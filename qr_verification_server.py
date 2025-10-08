#!/usr/bin/env python3
"""
QR Verification Server for e-Patta
==================================

A simple web server that handles QR code verification for e-Patta documents.
When QR codes are scanned, this server provides the verification page.
"""

import json
import os
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import webbrowser
import threading

class QRVerificationHandler(BaseHTTPRequestHandler):
    """HTTP request handler for QR verification"""
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        
        if parsed_path.path.startswith('/verify/'):
            # Extract patta number from URL
            patta_number = parsed_path.path.split('/verify/')[-1]
            self.handle_verification(patta_number)
        
        elif parsed_path.path == '/':
            self.serve_home_page()
        
        else:
            self.send_error(404, "Page not found")
    
    def handle_verification(self, patta_number):
        """Handle e-Patta verification request"""
        try:
            # Look for verification file
            verification_file = f"epatta_output/{patta_number}_verification.json"
            epatta_file = f"epatta_output/{patta_number}_epatta.json"
            
            if os.path.exists(verification_file) and os.path.exists(epatta_file):
                # Load verification data
                with open(verification_file, 'r', encoding='utf-8') as f:
                    verification_data = json.load(f)
                
                with open(epatta_file, 'r', encoding='utf-8') as f:
                    epatta_data = json.load(f)
                
                # Serve verification page
                self.serve_verification_page(verification_data, epatta_data)
            
            else:
                self.serve_not_found_page(patta_number)
        
        except Exception as e:
            self.send_error(500, f"Server error: {e}")
    
    def serve_verification_page(self, verification_data, epatta_data):
        """Serve the verification page"""
        coordinates = verification_data['coordinates']
        maps_url = coordinates['google_maps_url']
        
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>e-Patta Verification - {verification_data['patta_number']} | Government of India</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        body {{
            font-family: 'Inter', 'Segoe UI', sans-serif;
            margin: 0;
            padding: 20px;
            background: #f8f9fa;
            color: #212529;
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 700px;
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
            border-bottom: 4px solid #4CAF50;
        }}
        
        .emblem {{
            width: 50px;
            height: 50px;
            margin: 0 auto 10px;
            background: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            color: #1565C0;
            font-weight: bold;
        }}
        
        .gov-title {{
            font-size: 1.5em;
            font-weight: 600;
            margin: 0 0 5px 0;
        }}
        
        .verification-title {{
            font-size: 1.2em;
            font-weight: 500;
            margin: 0;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        .verification-badge {{
            background: rgba(255,255,255,0.15);
            padding: 10px 20px;
            border-radius: 6px;
            margin-top: 15px;
            display: inline-block;
            font-weight: 600;
            border: 1px solid rgba(255,255,255,0.3);
        }}
        .content {{
            padding: 30px;
        }}
        .info-card {{
            background: #f8f9fa;
            border-left: 4px solid #4CAF50;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
        }}
        .info-card .label {{
            font-weight: bold;
            color: #2E7D32;
            margin-bottom: 5px;
        }}
        .info-card .value {{
            color: #333;
            font-size: 1.1em;
        }}
        .maps-button {{
            display: block;
            background: #4CAF50;
            color: white;
            padding: 15px 25px;
            text-decoration: none;
            border-radius: 25px;
            font-weight: bold;
            text-align: center;
            margin: 20px 0;
            transition: all 0.3s ease;
        }}
        .maps-button:hover {{
            background: #45a049;
            transform: translateY(-2px);
        }}
        .coordinates {{
            background: #e8f5e8;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            margin: 20px 0;
        }}
        .status {{
            text-align: center;
            padding: 20px;
            background: #d4edda;
            border-radius: 10px;
            margin-bottom: 20px;
        }}
        .status .icon {{
            font-size: 3em;
            margin-bottom: 10px;
        }}
        .footer {{
            text-align: center;
            padding: 20px;
            background: #f8f9fa;
            color: #666;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="government-header">
            <div class="emblem">✓</div>
            <div class="gov-title">Government of India | भारत सरकार</div>
            <div class="verification-title">e-Patta Certificate Verification</div>
            <div class="verification-badge">Certificate No: {verification_data['patta_number']}</div>
        </div>
        
        <div class="content">
            <div class="status">
                <div class="icon">🏛️</div>
                <h2>Valid Forest Rights Certificate</h2>
                <p>This e-Patta has been digitally verified and is authentic.</p>
            </div>
            
            <div class="info-card">
                <div class="label">Claimant Name</div>
                <div class="value">{verification_data['claimant_name']}</div>
            </div>
            
            <div class="info-card">
                <div class="label">Tribe/Community</div>
                <div class="value">{verification_data['tribe']}</div>
            </div>
            
            <div class="info-card">
                <div class="label">Location</div>
                <div class="value">{verification_data['village']}, {verification_data['district']}, {verification_data['state']}</div>
            </div>
            
            <div class="info-card">
                <div class="label">Claim Type</div>
                <div class="value">{verification_data['claim_type']}</div>
            </div>
            
            <div class="info-card">
                <div class="label">Land Area</div>
                <div class="value">{verification_data['land_area']} hectares</div>
            </div>
            
            <div class="coordinates">
                <h3>📍 Geo-Coordinates</h3>
                <p><strong>Latitude:</strong> {coordinates['latitude']:.6f}</p>
                <p><strong>Longitude:</strong> {coordinates['longitude']:.6f}</p>
            </div>
            
            <a href="{maps_url}" target="_blank" class="maps-button" onclick="trackMapClick()">
                🗺️ View Location on Google Maps
            </a>
            
            <div class="info-card">
                <div class="label">Issue Date</div>
                <div class="value">{verification_data['issue_date']}</div>
            </div>
            
            <div class="info-card">
                <div class="label">Issuing Authority</div>
                <div class="value">{verification_data['authority']['name']}<br>
                {verification_data['authority']['designation']}</div>
            </div>
            
            <div class="info-card">
                <div class="label">Digital Signature</div>
                <div class="value">{verification_data['digital_signature']}</div>
            </div>
        </div>
        
        <div class="footer">
            Verified on {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}<br>
            Forest Rights Act - Digital Verification System
        </div>
    </div>
    
    <script>
        function trackMapClick() {{
            console.log('Opening Google Maps for coordinates: {coordinates["latitude"]}, {coordinates["longitude"]}');
            // You can add analytics tracking here
        }}
        
        // Auto-refresh verification status
        setTimeout(function() {{
            document.querySelector('.status').innerHTML = 
                '<div class="icon">✅</div><h2>Verification Complete</h2><p>e-Patta successfully verified at ' + 
                new Date().toLocaleTimeString() + '</p>';
        }}, 2000);
    </script>
</body>
</html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))
    
    def serve_not_found_page(self, patta_number):
        """Serve page when patta is not found"""
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>e-Patta Not Found</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background: #f5f5f5;
        }}
        .container {{
            max-width: 500px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        .error-icon {{
            font-size: 4em;
            color: #f44336;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="error-icon">❌</div>
        <h1>e-Patta Not Found</h1>
        <p>The e-Patta with number <strong>{patta_number}</strong> could not be found in our records.</p>
        <p>Please verify the QR code or contact the issuing authority.</p>
    </div>
</body>
</html>
        """
        
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))
    
    def serve_home_page(self):
        """Serve the home page"""
        html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>e-Patta Verification System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
        }
        h1 { font-size: 3em; margin-bottom: 20px; }
        p { font-size: 1.2em; margin-bottom: 30px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏛️ e-Patta Verification</h1>
        <p>Forest Rights Act - Digital Certificate Verification System</p>
        <p>Scan a QR code from an e-Patta document to verify its authenticity and view location details.</p>
    </div>
</body>
</html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

def start_verification_server(port=8080):
    """Start the QR verification server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, QRVerificationHandler)
    
    print(f"🌐 QR Verification Server starting on port {port}")
    print(f"📱 Access at: http://localhost:{port}")
    print(f"🔍 Verification URL format: http://localhost:{port}/verify/PATTA_NUMBER")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        httpd.shutdown()

def main():
    """Main function to start the server"""
    import argparse
    
    parser = argparse.ArgumentParser(description='e-Patta QR Verification Server')
    parser.add_argument('--port', '-p', type=int, default=8080, help='Server port (default: 8080)')
    parser.add_argument('--open', '-o', action='store_true', help='Open browser automatically')
    
    args = parser.parse_args()
    
    if args.open:
        # Open browser in a separate thread
        def open_browser():
            import time
            time.sleep(1)  # Wait for server to start
            webbrowser.open(f'http://localhost:{args.port}')
        
        threading.Thread(target=open_browser, daemon=True).start()
    
    start_verification_server(args.port)

if __name__ == "__main__":
    main()