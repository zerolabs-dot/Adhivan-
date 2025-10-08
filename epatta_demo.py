#!/usr/bin/env python3
"""
Complete e-Patta System Demo
===========================

Demonstrates the full e-Patta digitization workflow:
1. OCR + NER processing of FRA claims
2. e-Patta generation with QR codes
3. QR verification system
4. Google Maps integration
5. Mobile-scannable QR codes
"""

import os
import json
import webbrowser
import subprocess
import time
from datetime import datetime

def print_banner():
    """Print demo banner"""
    banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                           e-PATTA SYSTEM DEMO                               ║
║                     Digital Forest Rights Certificates                      ║
║                                                                              ║
║  🏛️ Complete digitization workflow for FRA claims                           ║
║  📱 QR codes for mobile verification                                        ║
║  🗺️ Google Maps integration                                                 ║
║  🔐 Digital signatures and verification                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def demo_ocr_processing():
    """Demonstrate OCR processing"""
    print("\n" + "="*80)
    print("📄 STEP 1: OCR + NER PROCESSING")
    print("="*80)
    
    print("\n🔍 Processing FRA claim document...")
    print("   Input: sample_fra_claim.txt")
    
    # Import and process
    from ocr_ner_digitization import OCRNERPipeline
    
    pipeline = OCRNERPipeline()
    result = pipeline.process_document("sample_fra_claim.txt")
    
    if result['success']:
        claim_data = result['claim_data']
        print(f"\n✅ Processing successful!")
        print(f"   Claimant: {claim_data.get('claimant_name', 'N/A')}")
        print(f"   Village: {claim_data.get('village', 'N/A')}")
        print(f"   District: {claim_data.get('district', 'N/A')}")
        print(f"   State: {claim_data.get('state', 'N/A')}")
        print(f"   Confidence: {claim_data.get('confidence_score', 0):.2f}")
        
        return result
    else:
        print(f"❌ Processing failed: {result.get('error', 'Unknown error')}")
        return None

def demo_epatta_generation(claim_result):
    """Demonstrate e-Patta generation"""
    print("\n" + "="*80)
    print("🏛️ STEP 2: e-PATTA GENERATION")
    print("="*80)
    
    if not claim_result:
        print("❌ Cannot generate e-Patta without valid claim data")
        return None
    
    print("\n📋 Generating digital land certificate...")
    
    from epatta_generator import EpattaGenerator
    
    generator = EpattaGenerator()
    
    # Generate e-Patta
    epatta_document, qr_image = generator.create_epatta_document(claim_result['claim_data'])
    
    # Save files
    epatta_files = generator.save_epatta_files(epatta_document, qr_image)
    
    print(f"✅ e-Patta generated successfully!")
    print(f"\n📄 Patta Details:")
    print(f"   Number: {epatta_document['patta_number']}")
    print(f"   Claimant: {epatta_document['claimant_details']['name']}")
    print(f"   Location: {epatta_document['claimant_details']['village']}, {epatta_document['claimant_details']['district']}")
    print(f"   Area: {epatta_document['land_details']['area']} hectares")
    print(f"   Coordinates: {epatta_document['land_details']['coordinates']}")
    
    print(f"\n📁 Generated Files:")
    for file_type, file_path in epatta_files.items():
        print(f"   • {file_type}: {file_path}")
    
    return epatta_document, epatta_files

def demo_qr_verification(epatta_document):
    """Demonstrate QR verification system"""
    print("\n" + "="*80)
    print("📱 STEP 3: QR VERIFICATION SYSTEM")
    print("="*80)
    
    if not epatta_document:
        print("❌ Cannot demo verification without e-Patta")
        return
    
    patta_number = epatta_document['patta_number']
    verification_url = f"http://localhost:8080/verify/{patta_number}"
    
    print(f"\n🔍 QR Code Information:")
    print(f"   Patta Number: {patta_number}")
    print(f"   Verification URL: {verification_url}")
    print(f"   Google Maps: {epatta_document['land_details']['google_maps_url']}")
    
    # Start verification server
    print(f"\n🌐 Starting QR verification server...")
    
    try:
        # Start server in background
        server_process = subprocess.Popen([
            "python", "qr_verification_server.py", "--port", "8080"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait a moment for server to start
        time.sleep(2)
        
        print(f"✅ Verification server started on port 8080")
        print(f"📱 Server URL: http://localhost:8080")
        print(f"🔍 Verification URL: {verification_url}")
        
        return server_process, verification_url
        
    except Exception as e:
        print(f"❌ Failed to start server: {e}")
        return None, None

def demo_mobile_scanning(verification_url, epatta_files):
    """Demonstrate mobile QR scanning"""
    print("\n" + "="*80)
    print("📱 STEP 4: MOBILE QR SCANNING")
    print("="*80)
    
    if not verification_url:
        print("❌ Cannot demo mobile scanning without verification server")
        return
    
    print(f"\n📲 Mobile QR Code Scanning Demo:")
    print(f"   1. Open the QR code image: {epatta_files.get('qr_file', 'N/A')}")
    print(f"   2. Scan with any QR code scanner app")
    print(f"   3. The QR contains verification data and Google Maps link")
    print(f"   4. Scanning will open: {verification_url}")
    
    # Show QR code content
    qr_file = epatta_files.get('qr_file')
    if qr_file and os.path.exists(qr_file):
        print(f"\n📄 QR Code generated: {qr_file}")
        print(f"   File size: {os.path.getsize(qr_file)} bytes")
    
    # Ask if user wants to test verification
    test_verification = input(f"\n❓ Open verification page in browser? (y/n): ").lower().strip()
    if test_verification in ['y', 'yes']:
        print(f"🌐 Opening verification page...")
        webbrowser.open(verification_url)
        print(f"✅ Verification page opened in browser")

def demo_google_maps_integration(epatta_document):
    """Demonstrate Google Maps integration"""
    print("\n" + "="*80)
    print("🗺️ STEP 5: GOOGLE MAPS INTEGRATION")
    print("="*80)
    
    if not epatta_document:
        print("❌ Cannot demo maps without e-Patta")
        return
    
    coordinates = epatta_document['land_details']['coordinates']
    maps_url = epatta_document['land_details']['google_maps_url']
    
    print(f"\n📍 Location Information:")
    print(f"   Latitude: {coordinates[0]:.6f}")
    print(f"   Longitude: {coordinates[1]:.6f}")
    print(f"   Google Maps URL: {maps_url}")
    
    print(f"\n🗺️ Features:")
    print(f"   • Clickable coordinates in e-Patta")
    print(f"   • Direct Google Maps integration")
    print(f"   • Mobile-friendly map links")
    print(f"   • Precise location marking")
    
    # Ask if user wants to open maps
    open_maps = input(f"\n❓ Open location in Google Maps? (y/n): ").lower().strip()
    if open_maps in ['y', 'yes']:
        print(f"🌐 Opening Google Maps...")
        webbrowser.open(maps_url)
        print(f"✅ Location opened in Google Maps")

def demo_complete_workflow():
    """Run complete e-Patta workflow demo"""
    print_banner()
    
    print(f"\n🎯 This demo will show the complete e-Patta digitization workflow:")
    print(f"   1. OCR + NER processing of FRA claims")
    print(f"   2. e-Patta generation with unique numbers")
    print(f"   3. QR code generation for mobile verification")
    print(f"   4. Web-based verification system")
    print(f"   5. Google Maps integration")
    
    input(f"\n▶️  Press Enter to start the demo...")
    
    try:
        # Step 1: OCR Processing
        claim_result = demo_ocr_processing()
        
        if not claim_result:
            print(f"\n❌ Demo stopped due to OCR processing failure")
            return
        
        # Step 2: e-Patta Generation
        epatta_document, epatta_files = demo_epatta_generation(claim_result)
        
        if not epatta_document:
            print(f"\n❌ Demo stopped due to e-Patta generation failure")
            return
        
        # Step 3: QR Verification
        server_process, verification_url = demo_qr_verification(epatta_document)
        
        # Step 4: Mobile Scanning Demo
        demo_mobile_scanning(verification_url, epatta_files)
        
        # Step 5: Google Maps Integration
        demo_google_maps_integration(epatta_document)
        
        # Final Summary
        print(f"\n" + "="*80)
        print(f"🎉 DEMO COMPLETED SUCCESSFULLY!")
        print(f"="*80)
        
        print(f"\n📊 Summary:")
        print(f"   • e-Patta Number: {epatta_document['patta_number']}")
        print(f"   • Claimant: {epatta_document['claimant_details']['name']}")
        print(f"   • Location: {epatta_document['land_details']['coordinates']}")
        print(f"   • Verification URL: {verification_url}")
        
        print(f"\n📁 Generated Files:")
        for file_type, file_path in epatta_files.items():
            print(f"   • {file_type}: {file_path}")
        
        print(f"\n🚀 Next Steps:")
        print(f"   • View e-Patta: Open {epatta_files['html_file']}")
        print(f"   • Test QR Code: Scan {epatta_files['qr_file']}")
        print(f"   • Verify Online: Visit {verification_url}")
        print(f"   • View Location: Open Google Maps link")
        
        # Keep server running
        if server_process:
            print(f"\n🌐 Verification server is running...")
            print(f"   Press Ctrl+C to stop the server")
            
            try:
                server_process.wait()
            except KeyboardInterrupt:
                print(f"\n🛑 Stopping verification server...")
                server_process.terminate()
                print(f"✅ Server stopped")
        
    except KeyboardInterrupt:
        print(f"\n🛑 Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Demo failed with error: {e}")

def main():
    """Main demo function"""
    demo_complete_workflow()

if __name__ == "__main__":
    main()