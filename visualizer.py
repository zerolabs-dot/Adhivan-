#!/usr/bin/env python3
"""
Visualization Module for OCR + NER Results
==========================================

Creates visual representations of extracted FRA claim data including:
- Formatted text output
- HTML reports
- Console-based visualization
"""

import json
import os
from datetime import datetime
from typing import Dict, Any

class FRAClaimVisualizer:
    """Visualizes FRA claim extraction results"""
    
    def __init__(self):
        self.colors = {
            'header': '\033[95m',
            'blue': '\033[94m',
            'cyan': '\033[96m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'red': '\033[91m',
            'bold': '\033[1m',
            'underline': '\033[4m',
            'end': '\033[0m'
        }
    
    def colorize(self, text: str, color: str) -> str:
        """Add color to text for console output"""
        return f"{self.colors.get(color, '')}{text}{self.colors['end']}"
    
    def print_banner(self):
        """Print a nice banner"""
        banner = """
╔══════════════════════════════════════════════════════════════╗
║                    FRA CLAIM DIGITIZATION                    ║
║                   OCR + NER Pipeline Results                 ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(self.colorize(banner, 'cyan'))
    
    def visualize_console(self, result: Dict[str, Any]):
        """Display results in console with nice formatting"""
        self.print_banner()
        
        if not result.get('success'):
            print(self.colorize(f"❌ Processing Failed: {result.get('error', 'Unknown error')}", 'red'))
            return
        
        claim_data = result.get('claim_data', {})
        
        # Processing Summary
        print(self.colorize("📊 PROCESSING SUMMARY", 'header'))
        print("=" * 60)
        print(f"Status: {self.colorize('✅ SUCCESS', 'green')}")
        print(f"Processing Time: {result.get('processing_time_seconds', 0):.2f} seconds")
        print(f"Confidence Score: {self.colorize(f'{claim_data.get('confidence_score', 0):.2f}', 'yellow')}")
        
        needs_review = result.get('needs_review', False)
        review_status = "⚠️  NEEDS REVIEW" if needs_review else "✅ AUTO-APPROVED"
        review_color = 'yellow' if needs_review else 'green'
        print(f"Review Status: {self.colorize(review_status, review_color)}")
        print()
        
        # Extracted Information
        print(self.colorize("📋 EXTRACTED CLAIM INFORMATION", 'header'))
        print("=" * 60)
        
        fields = [
            ('Claim ID', 'claim_id', '�'),
            ('Claimant Name', 'claimant_name', '👤'),
            ('Tribe/Community', 'tribe', '🏘️'),
            ('Village', 'village', '🏡'),
            ('District', 'district', '🏛️'),
            ('State', 'state', '🗺️'),
            ('Claim Type', 'claim_type', '📄'),
            ('Land Area', 'land_area', '🌾'),
            ('Application Date', 'application_date', '📅'),
        ]
        
        for display_name, field_key, icon in fields:
            value = claim_data.get(field_key, '')
            if value:
                print(f"{icon} {self.colorize(display_name + ':', 'blue')} {self.colorize(value, 'bold')}")
            else:
                print(f"{icon} {self.colorize(display_name + ':', 'blue')} {self.colorize('Not Found', 'red')}")
        
        print()
        
        # Processing Details
        print(self.colorize("🔍 PROCESSING DETAILS", 'header'))
        print("=" * 60)
        print(f"Processing Timestamp: {claim_data.get('processing_timestamp', 'N/A')}")
        
        if 'total_files' in result:
            print(f"Total Files Processed: {result['total_files']}")
            print(f"Successful: {result['successful']}")
            print(f"Failed: {result['failed']}")
            print(f"Success Rate: {result['success_rate']:.1f}%")
        
        print()
        
        # Raw Text Preview
        raw_text = claim_data.get('raw_text', '')
        if raw_text:
            print(self.colorize("📝 RAW TEXT PREVIEW", 'header'))
            print("=" * 60)
            preview = raw_text[:300] + "..." if len(raw_text) > 300 else raw_text
            print(self.colorize(preview, 'cyan'))
            print()
    
    def generate_html_report(self, result: Dict[str, Any], output_path: str = "fra_claim_report.html"):
        """Generate HTML report"""
        claim_data = result.get('claim_data', {})
        
        html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FRA Claim Digitization Report</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
            font-weight: 300;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}
        .content {{
            padding: 30px;
        }}
        .section {{
            margin-bottom: 30px;
        }}
        .section h2 {{
            color: #333;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }}
        .info-card {{
            background: #f8f9fa;
            border-left: 4px solid #4CAF50;
            padding: 15px;
            border-radius: 5px;
        }}
        .info-card .label {{
            font-weight: bold;
            color: #555;
            margin-bottom: 5px;
        }}
        .info-card .value {{
            font-size: 1.1em;
            color: #333;
        }}
        .status {{
            display: inline-block;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: bold;
            text-transform: uppercase;
        }}
        .status.success {{
            background: #d4edda;
            color: #155724;
        }}
        .status.warning {{
            background: #fff3cd;
            color: #856404;
        }}
        .status.error {{
            background: #f8d7da;
            color: #721c24;
        }}
        .confidence-bar {{
            width: 100%;
            height: 20px;
            background: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
            margin-top: 10px;
        }}
        .confidence-fill {{
            height: 100%;
            background: linear-gradient(90deg, #ff4444, #ffaa00, #44ff44);
            transition: width 0.3s ease;
        }}
        .raw-text {{
            background: #f1f3f4;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 15px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            max-height: 200px;
            overflow-y: auto;
            white-space: pre-wrap;
        }}
        .timestamp {{
            text-align: center;
            color: #666;
            font-size: 0.9em;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #eee;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏛️ FRA Claim Report</h1>
            <p>Forest Rights Act - Digital Claim Processing</p>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>📊 Processing Summary</h2>
                <div class="info-grid">
                    <div class="info-card">
                        <div class="label">Processing Status</div>
                        <div class="value">
                            <span class="status {'success' if result.get('success') else 'error'}">
                                {'✅ Success' if result.get('success') else '❌ Failed'}
                            </span>
                        </div>
                    </div>
                    <div class="info-card">
                        <div class="label">Processing Time</div>
                        <div class="value">{result.get('processing_time_seconds', 0):.2f} seconds</div>
                    </div>
                    <div class="info-card">
                        <div class="label">Confidence Score</div>
                        <div class="value">
                            {claim_data.get('confidence_score', 0):.2f}
                            <div class="confidence-bar">
                                <div class="confidence-fill" style="width: {claim_data.get('confidence_score', 0) * 100}%"></div>
                            </div>
                        </div>
                    </div>
                    <div class="info-card">
                        <div class="label">Review Status</div>
                        <div class="value">
                            <span class="status {'warning' if result.get('needs_review') else 'success'}">
                                {'⚠️ Needs Review' if result.get('needs_review') else '✅ Auto-Approved'}
                            </span>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>📋 Extracted Information</h2>
                <div class="info-grid">
                    <div class="info-card">
                        <div class="label">🆔 Claim ID</div>
                        <div class="value">{claim_data.get('claim_id', 'Not Found')}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">👤 Claimant Name</div>
                        <div class="value">{claim_data.get('claimant_name', 'Not Found')}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">🏘️ Tribe/Community</div>
                        <div class="value">{claim_data.get('tribe', 'Not Found')}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">🏡 Village</div>
                        <div class="value">{claim_data.get('village', 'Not Found')}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">🏛️ District</div>
                        <div class="value">{claim_data.get('district', 'Not Found')}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">🗺️ State</div>
                        <div class="value">{claim_data.get('state', 'Not Found')}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">📄 Claim Type</div>
                        <div class="value">{claim_data.get('claim_type', 'Not Found')}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">🌾 Land Area</div>
                        <div class="value">{claim_data.get('land_area', 'Not Found')} {'hectares' if claim_data.get('land_area') else ''}</div>
                    </div>
                    <div class="info-card">
                        <div class="label">📅 Application Date</div>
                        <div class="value">{claim_data.get('application_date', 'Not Found')}</div>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>📝 Raw Extracted Text</h2>
                <div class="raw-text">{claim_data.get('raw_text', 'No text available')}</div>
            </div>
            
            <div class="timestamp">
                Report generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            </div>
        </div>
    </div>
</body>
</html>
        """
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_template)
        
        return output_path
    
    def create_summary_table(self, results: list):
        """Create a summary table for batch processing results"""
        if not results:
            return
        
        print(self.colorize("📊 BATCH PROCESSING SUMMARY", 'header'))
        print("=" * 80)
        
        # Table header
        header = f"{'File':<30} {'Status':<10} {'Confidence':<12} {'Review':<10}"
        print(self.colorize(header, 'bold'))
        print("-" * 80)
        
        # Table rows
        for result in results:
            filename = os.path.basename(result.get('file_path', 'Unknown'))[:28]
            status = "✅ Success" if result.get('success') else "❌ Failed"
            
            if result.get('success'):
                confidence = f"{result['claim_data']['confidence_score']:.2f}"
                review = "⚠️  Review" if result.get('needs_review') else "✅ OK"
            else:
                confidence = "N/A"
                review = "N/A"
            
            row = f"{filename:<30} {status:<10} {confidence:<12} {review:<10}"
            print(row)

def main():
    """Main function to demonstrate visualization"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Visualize FRA Claim Processing Results')
    parser.add_argument('--input', '-i', help='JSON result file to visualize')
    parser.add_argument('--html', action='store_true', help='Generate HTML report')
    parser.add_argument('--output', '-o', help='Output HTML file path')
    
    args = parser.parse_args()
    
    visualizer = FRAClaimVisualizer()
    
    if args.input and os.path.exists(args.input):
        # Load and visualize existing result
        with open(args.input, 'r', encoding='utf-8') as f:
            result = json.load(f)
        
        visualizer.visualize_console(result)
        
        if args.html:
            output_path = args.output or 'fra_claim_report.html'
            html_file = visualizer.generate_html_report(result, output_path)
            print(f"\n📄 HTML report generated: {html_file}")
    
    else:
        # Demo with sample data
        sample_result = {
            'success': True,
            'claim_data': {
                'claim_id': 'FRA/2023/MP/12345',
                'claimant_name': 'Ramesh Kumar Gond',
                'tribe': 'Gond',
                'village': 'Khairwani',
                'district': 'Mandla',
                'state': 'Madhya Pradesh',
                'claim_type': 'IFR',
                'land_area': '2.5',
                'application_date': '15-07-2023',
                'confidence_score': 0.92,
                'processing_timestamp': datetime.now().isoformat(),
                'raw_text': 'Forest Rights Act Claim Application\n\nClaim ID: FRA/2023/MP/12345...'
            },
            'processing_time_seconds': 1.25,
            'needs_review': False
        }
        
        print("🎯 Displaying sample FRA claim visualization:")
        visualizer.visualize_console(sample_result)
        
        if args.html:
            output_path = args.output or 'sample_fra_report.html'
            html_file = visualizer.generate_html_report(sample_result, output_path)
            print(f"\n📄 Sample HTML report generated: {html_file}")

if __name__ == "__main__":
    main()