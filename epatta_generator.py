#!/usr/bin/env python3
"""
E-Patta Generator for FRA Claims
===============================

Generates digitalized land records (e-Patta) with:
- Unique patta numbers
- QR codes for verification
- Geo-coordinates integration
- Authority signatures
- Google Maps integration
- Mobile-scannable QR codes
"""

import os
import json
import uuid
import qrcode
from datetime import datetime
from typing import Dict, Any, Tuple
import base64
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import hashlib

class EpattaGenerator:
    """Generates digital land records (e-Patta) for FRA claims"""
    
    def __init__(self):
        self.base_url = "https://fra-epatta.gov.in/verify/"  # Base URL for QR verification
        self.authority_info = {
            'name': 'Forest Rights Committee',
            'designation': 'Sub-Divisional Level Committee',
            'office': 'District Collector Office',
            'signature_text': 'Digitally Signed'
        }
    
    def generate_unique_patta_number(self, claim_data: Dict[str, Any]) -> str:
        """Generate unique patta number based on claim data"""
        # Format: FRA-STATE-DISTRICT-YEAR-SEQUENCE
        state_code = self._get_state_code(claim_data.get('state', ''))
        district_code = self._get_district_code(claim_data.get('district', ''))
        year = datetime.now().year
        
        # Generate sequence based on hash of claim data
        claim_hash = hashlib.md5(
            f"{claim_data.get('claimant_name', '')}{claim_data.get('village', '')}{datetime.now().isoformat()}".encode()
        ).hexdigest()[:6].upper()
        
        patta_number = f"FRA-{state_code}-{district_code}-{year}-{claim_hash}"
        return patta_number
    
    def _get_state_code(self, state: str) -> str:
        """Get state code from state name"""
        state_codes = {
            'madhya pradesh': 'MP',
            'odisha': 'OD',
            'telangana': 'TG',
            'west bengal': 'WB',
            'jharkhand': 'JH',
            'chhattisgarh': 'CG',
            'maharashtra': 'MH'
        }
        return state_codes.get(state.lower(), 'XX')
    
    def _get_district_code(self, district: str) -> str:
        """Get district code from district name"""
        # Generate 3-letter code from district name
        if len(district) >= 3:
            return district[:3].upper()
        return district.upper().ljust(3, 'X')
    
    def generate_geo_coordinates(self, village: str, district: str, state: str) -> Tuple[float, float]:
        """Generate approximate geo-coordinates for the location"""
        # In a real system, this would query a geospatial database
        # For demo, we'll generate coordinates based on known locations
        
        location_coords = {
            # Madhya Pradesh
            ('khairwani', 'mandla', 'madhya pradesh'): (22.5937, 80.3656),
            ('mandla', 'mandla', 'madhya pradesh'): (22.5937, 80.3656),
            
            # Default coordinates for different states
            'madhya pradesh': (23.2599, 77.4126),
            'odisha': (20.9517, 85.0985),
            'telangana': (18.1124, 79.0193),
            'west bengal': (22.9868, 87.8550),
            'jharkhand': (23.6102, 85.2799),
        }
        
        # Try exact match first
        key = (village.lower(), district.lower(), state.lower())
        if key in location_coords:
            return location_coords[key]
        
        # Fall back to state-level coordinates
        state_key = state.lower()
        if state_key in location_coords:
            base_lat, base_lon = location_coords[state_key]
            # Add small random offset for village-level precision
            import random
            lat_offset = random.uniform(-0.1, 0.1)
            lon_offset = random.uniform(-0.1, 0.1)
            return (base_lat + lat_offset, base_lon + lon_offset)
        
        # Default coordinates (center of India)
        return (20.5937, 78.9629)
    
    def create_verification_data(self, claim_data: Dict[str, Any], patta_number: str, 
                               coordinates: Tuple[float, float]) -> Dict[str, Any]:
        """Create data structure for QR code verification"""
        verification_data = {
            'patta_number': patta_number,
            'claimant_name': claim_data.get('claimant_name', ''),
            'tribe': claim_data.get('tribe', ''),
            'village': claim_data.get('village', ''),
            'district': claim_data.get('district', ''),
            'state': claim_data.get('state', ''),
            'claim_type': claim_data.get('claim_type', ''),
            'land_area': claim_data.get('land_area', ''),
            'application_date': claim_data.get('application_date', ''),
            'issue_date': datetime.now().strftime('%d-%m-%Y'),
            'coordinates': {
                'latitude': coordinates[0],
                'longitude': coordinates[1],
                'google_maps_url': f"https://www.google.com/maps?q={coordinates[0]},{coordinates[1]}"
            },
            'authority': self.authority_info,
            'verification_url': f"{self.base_url}{patta_number}",
            'digital_signature': self._generate_digital_signature(claim_data, patta_number),
            'qr_generated_at': datetime.now().isoformat()
        }
        
        return verification_data
    
    def _generate_digital_signature(self, claim_data: Dict[str, Any], patta_number: str) -> str:
        """Generate digital signature for the patta"""
        # In a real system, this would use proper cryptographic signing
        signature_data = f"{patta_number}{claim_data.get('claimant_name', '')}{datetime.now().date()}"
        signature_hash = hashlib.sha256(signature_data.encode()).hexdigest()
        return f"DS-{signature_hash[:16].upper()}"
    
    def generate_qr_code(self, verification_data: Dict[str, Any]) -> Image.Image:
        """Generate QR code containing verification data"""
        # Create QR code with verification URL and basic data
        qr_data = {
            'url': verification_data['verification_url'],
            'patta': verification_data['patta_number'],
            'name': verification_data['claimant_name'],
            'coords': f"{verification_data['coordinates']['latitude']},{verification_data['coordinates']['longitude']}",
            'maps': verification_data['coordinates']['google_maps_url']
        }
        
        qr_string = json.dumps(qr_data, separators=(',', ':'))
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_string)
        qr.make(fit=True)
        
        # Create QR code image
        qr_img = qr.make_image(fill_color="black", back_color="white")
        return qr_img
    
    def create_epatta_document(self, claim_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create complete e-Patta document"""
        # Generate unique patta number
        patta_number = self.generate_unique_patta_number(claim_data)
        
        # Generate geo-coordinates
        coordinates = self.generate_geo_coordinates(
            claim_data.get('village', ''),
            claim_data.get('district', ''),
            claim_data.get('state', '')
        )
        
        # Create verification data
        verification_data = self.create_verification_data(claim_data, patta_number, coordinates)
        
        # Generate QR code
        qr_image = self.generate_qr_code(verification_data)
        
        # Create e-Patta document
        epatta_document = {
            'patta_number': patta_number,
            'issue_date': datetime.now().strftime('%d-%m-%Y'),
            'claimant_details': {
                'name': claim_data.get('claimant_name', ''),
                'tribe': claim_data.get('tribe', ''),
                'village': claim_data.get('village', ''),
                'district': claim_data.get('district', ''),
                'state': claim_data.get('state', '')
            },
            'land_details': {
                'claim_type': claim_data.get('claim_type', ''),
                'area': claim_data.get('land_area', ''),
                'coordinates': coordinates,
                'google_maps_url': f"https://www.google.com/maps?q={coordinates[0]},{coordinates[1]}"
            },
            'verification': verification_data,
            'qr_code_data': qr_string if 'qr_string' in locals() else '',
            'authority': self.authority_info,
            'status': 'ACTIVE',
            'created_at': datetime.now().isoformat()
        }
        
        return epatta_document, qr_image
    
    def generate_epatta_html(self, epatta_document: Dict[str, Any], qr_image: Image.Image) -> str:
        """Generate HTML representation of e-Patta"""
        # Convert QR code to base64 for embedding
        buffered = BytesIO()
        qr_image.save(buffered, format="PNG")
        qr_base64 = base64.b64encode(buffered.getvalue()).decode()
        
        coordinates = epatta_document['land_details']['coordinates']
        maps_url = epatta_document['land_details']['google_maps_url']
        
        html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>e-Patta Certificate - {epatta_document['patta_number']} | Government of India</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        body {{
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f8f9fa;
            color: #212529;
            line-height: 1.6;
        }}
        
        .epatta-container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border: 2px solid #1565C0;
            box-shadow: 0 4px 20px rgba(21, 101, 192, 0.1);
        }}
        
        .government-header {{
            background: linear-gradient(135deg, #1565C0 0%, #0D47A1 100%);
            color: white;
            padding: 25px 40px;
            text-align: center;
            border-bottom: 4px solid #FF9800;
        }}
        
        .emblem {{
            width: 60px;
            height: 60px;
            margin: 0 auto 15px;
            background: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            color: #1565C0;
            font-weight: bold;
        }}
        
        .gov-title {{
            font-size: 1.8em;
            font-weight: 600;
            margin: 0 0 5px 0;
            letter-spacing: 0.5px;
        }}
        
        .ministry {{
            font-size: 1.1em;
            margin: 0 0 15px 0;
            opacity: 0.95;
            font-weight: 400;
        }}
        
        .certificate-title {{
            font-size: 1.4em;
            font-weight: 700;
            margin: 0;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .patta-number {{
            background: rgba(255,255,255,0.15);
            padding: 12px 25px;
            border-radius: 6px;
            margin-top: 20px;
            display: inline-block;
            font-weight: 600;
            font-size: 1.1em;
            border: 1px solid rgba(255,255,255,0.3);
        }}
        .content {{
            padding: 30px;
        }}
        .section {{
            margin-bottom: 30px;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 20px;
            background: #f9f9f9;
        }}
        .section h2 {{
            color: #2E7D32;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-size: 1.5em;
        }}
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
        }}
        .info-item {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #4CAF50;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .info-item .label {{
            font-weight: bold;
            color: #2E7D32;
            margin-bottom: 5px;
            font-size: 0.9em;
            text-transform: uppercase;
        }}
        .info-item .value {{
            font-size: 1.1em;
            color: #333;
        }}
        .qr-section {{
            text-align: center;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        .qr-code {{
            margin: 20px 0;
            padding: 20px;
            background: white;
            border-radius: 10px;
            display: inline-block;
            box-shadow: 0 3px 10px rgba(0,0,0,0.2);
        }}
        .coordinates-link {{
            display: inline-block;
            background: #4CAF50;
            color: white;
            padding: 12px 25px;
            text-decoration: none;
            border-radius: 25px;
            font-weight: bold;
            margin: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 3px 10px rgba(76, 175, 80, 0.3);
        }}
        .coordinates-link:hover {{
            background: #45a049;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
        }}
        .signature-section {{
            background: linear-gradient(135deg, #f5f5f5 0%, #e8e8e8 100%);
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            margin-top: 30px;
        }}
        .signature {{
            font-style: italic;
            color: #2E7D32;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .authority-info {{
            font-size: 0.9em;
            color: #666;
        }}
        .status-badge {{
            display: inline-block;
            background: #4CAF50;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: bold;
            text-transform: uppercase;
            font-size: 0.9em;
        }}
        .watermark {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(-45deg);
            font-size: 6em;
            color: rgba(46, 125, 50, 0.05);
            font-weight: bold;
            z-index: -1;
            pointer-events: none;
        }}
        @media print {{
            body {{ background: white; }}
            .epatta-container {{ box-shadow: none; border: 2px solid #2E7D32; }}
        }}
    </style>
</head>
<body>
    <div class="watermark">e-PATTA</div>
    
    <div class="epatta-container">
        <div class="government-header">
            <div class="emblem">🇮🇳</div>
            <div class="gov-title">भारत सरकार | Government of India</div>
            <div class="ministry">Ministry of Tribal Affairs</div>
            <div class="certificate-title">Digital Forest Rights Certificate (e-Patta)</div>
            <div class="patta-number">Certificate No: {epatta_document['patta_number']}</div>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>👤 Claimant Information</h2>
                <div class="info-grid">
                    <div class="info-item">
                        <div class="label">Full Name</div>
                        <div class="value">{epatta_document['claimant_details']['name']}</div>
                    </div>
                    <div class="info-item">
                        <div class="label">Tribe/Community</div>
                        <div class="value">{epatta_document['claimant_details']['tribe']}</div>
                    </div>
                    <div class="info-item">
                        <div class="label">Village</div>
                        <div class="value">{epatta_document['claimant_details']['village']}</div>
                    </div>
                    <div class="info-item">
                        <div class="label">District</div>
                        <div class="value">{epatta_document['claimant_details']['district']}</div>
                    </div>
                    <div class="info-item">
                        <div class="label">State</div>
                        <div class="value">{epatta_document['claimant_details']['state']}</div>
                    </div>
                    <div class="info-item">
                        <div class="label">Status</div>
                        <div class="value"><span class="status-badge">{epatta_document['status']}</span></div>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>🌾 Land Details</h2>
                <div class="info-grid">
                    <div class="info-item">
                        <div class="label">Claim Type</div>
                        <div class="value">{epatta_document['land_details']['claim_type']}</div>
                    </div>
                    <div class="info-item">
                        <div class="label">Land Area</div>
                        <div class="value">{epatta_document['land_details']['area']} hectares</div>
                    </div>
                    <div class="info-item">
                        <div class="label">Coordinates</div>
                        <div class="value">
                            Lat: {coordinates[0]:.6f}<br>
                            Lon: {coordinates[1]:.6f}
                        </div>
                    </div>
                    <div class="info-item">
                        <div class="label">Issue Date</div>
                        <div class="value">{epatta_document['issue_date']}</div>
                    </div>
                </div>
                
                <div style="text-align: center; margin-top: 20px;">
                    <a href="{maps_url}" target="_blank" class="coordinates-link">
                        🗺️ View on Google Maps
                    </a>
                </div>
            </div>
            
            <div class="section qr-section">
                <h2>📱 QR Code Verification</h2>
                <p>Scan this QR code with your mobile device to verify the e-Patta and view location details</p>
                
                <div class="qr-code">
                    <img src="data:image/png;base64,{qr_base64}" alt="QR Code" style="max-width: 200px;">
                </div>
                
                <p><strong>Verification URL:</strong><br>
                <a href="{epatta_document['verification']['verification_url']}" target="_blank">
                    {epatta_document['verification']['verification_url']}
                </a></p>
                
                <p><strong>Digital Signature:</strong> {epatta_document['verification']['digital_signature']}</p>
            </div>
            
            <div class="signature-section">
                <div class="signature">
                    {epatta_document['authority']['signature_text']}
                </div>
                <div class="authority-info">
                    <strong>{epatta_document['authority']['name']}</strong><br>
                    {epatta_document['authority']['designation']}<br>
                    {epatta_document['authority']['office']}<br>
                    Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
                </div>
            </div>
        </div>
    </div>
    
    <script>
        // Add click handler for coordinates
        document.addEventListener('DOMContentLoaded', function() {{
            const coordsElements = document.querySelectorAll('.coordinates-link');
            coordsElements.forEach(function(element) {{
                element.addEventListener('click', function(e) {{
                    // Track click for analytics (if needed)
                    console.log('Opening Google Maps for coordinates: {coordinates[0]}, {coordinates[1]}');
                }});
            }});
        }});
    </script>
</body>
</html>
        """
        
        return html_template
    
    def save_epatta_files(self, epatta_document: Dict[str, Any], qr_image: Image.Image, 
                         output_dir: str = "epatta_output") -> Dict[str, str]:
        """Save e-Patta files (JSON, HTML, QR code)"""
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        patta_number = epatta_document['patta_number']
        
        # Save JSON data
        json_file = os.path.join(output_dir, f"{patta_number}_epatta.json")
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(epatta_document, f, indent=2, ensure_ascii=False)
        
        # Save QR code image
        qr_file = os.path.join(output_dir, f"{patta_number}_qr.png")
        qr_image.save(qr_file)
        
        # Save HTML document
        html_content = self.generate_epatta_html(epatta_document, qr_image)
        html_file = os.path.join(output_dir, f"{patta_number}_epatta.html")
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Save verification data for QR scanning
        verification_file = os.path.join(output_dir, f"{patta_number}_verification.json")
        with open(verification_file, 'w', encoding='utf-8') as f:
            json.dump(epatta_document['verification'], f, indent=2, ensure_ascii=False)
        
        return {
            'json_file': json_file,
            'html_file': html_file,
            'qr_file': qr_file,
            'verification_file': verification_file
        }

def main():
    """Demo function for e-Patta generation"""
    # Sample claim data
    sample_claim = {
        'claimant_name': 'Ramesh Kumar Gond',
        'tribe': 'Gond',
        'village': 'Khairwani',
        'district': 'Mandla',
        'state': 'Madhya Pradesh',
        'claim_type': 'IFR',
        'land_area': '2.5',
        'application_date': '15-07-2023'
    }
    
    print("🏛️ Generating e-Patta for FRA Claim...")
    
    # Create e-Patta generator
    generator = EpattaGenerator()
    
    # Generate e-Patta
    epatta_document, qr_image = generator.create_epatta_document(sample_claim)
    
    # Save files
    files = generator.save_epatta_files(epatta_document, qr_image)
    
    print(f"✅ e-Patta generated successfully!")
    print(f"📄 Patta Number: {epatta_document['patta_number']}")
    print(f"📁 Files saved:")
    for file_type, file_path in files.items():
        print(f"   • {file_type}: {file_path}")
    
    print(f"\n🗺️ Coordinates: {epatta_document['land_details']['coordinates']}")
    print(f"🌐 Google Maps: {epatta_document['land_details']['google_maps_url']}")
    print(f"📱 QR Verification: {epatta_document['verification']['verification_url']}")

if __name__ == "__main__":
    main()