#!/usr/bin/env python3
"""
Demo Script for FRA Claim Digitization System
=============================================

This script demonstrates all capabilities of the OCR + NER pipeline:
1. Console-based processing with visualization
2. GUI application launch
3. HTML report generation
4. Batch processing capabilities
"""

import os
import sys
import json
import time
from datetime import datetime

def print_banner():
    """Print demo banner"""
    banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                          FRA CLAIM DIGITIZATION DEMO                        ║
║                             OCR + NER Pipeline                              ║
║                                                                              ║
║  🏛️ Forest Rights Act - Digital Claim Processing System                     ║
║  📄 Converts scanned documents to structured data                           ║
║  🤖 Uses OCR + Named Entity Recognition                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def demo_console_processing():
    """Demonstrate console-based processing"""
    print("\n" + "="*80)
    print("🖥️  CONSOLE PROCESSING DEMO")
    print("="*80)
    
    print("\n1️⃣ Processing sample FRA claim document...")
    print("   File: sample_fra_claim.txt")
    
    # Import and run pipeline
    from ocr_ner_digitization import OCRNERPipeline
    from visualizer import FRAClaimVisualizer
    
    pipeline = OCRNERPipeline()
    visualizer = FRAClaimVisualizer()
    
    # Process document
    result = pipeline.process_document("sample_fra_claim.txt")
    
    print("\n2️⃣ Displaying results with visualization...")
    time.sleep(1)
    
    # Show visualization
    visualizer.visualize_console(result)
    
    return result

def demo_html_report(result):
    """Generate and show HTML report"""
    print("\n" + "="*80)
    print("🌐 HTML REPORT GENERATION")
    print("="*80)
    
    from visualizer import FRAClaimVisualizer
    visualizer = FRAClaimVisualizer()
    
    print("\n📄 Generating HTML report...")
    html_file = visualizer.generate_html_report(result, "demo_report.html")
    
    print(f"✅ HTML report generated: {html_file}")
    print("   You can open this file in your web browser to view the formatted report.")
    
    return html_file

def demo_json_export(result):
    """Export results as JSON"""
    print("\n" + "="*80)
    print("💾 JSON EXPORT DEMO")
    print("="*80)
    
    json_file = "demo_results.json"
    
    print(f"\n📁 Exporting results to: {json_file}")
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print("✅ JSON export completed!")
    
    # Show sample of JSON content
    print("\n📋 Sample JSON content:")
    print("-" * 40)
    
    sample_data = {
        "claim_id": result['claim_data'].get('claim_id', ''),
        "claimant_name": result['claim_data'].get('claimant_name', ''),
        "confidence_score": result['claim_data'].get('confidence_score', 0),
        "processing_time": result.get('processing_time_seconds', 0)
    }
    
    print(json.dumps(sample_data, indent=2))
    
    return json_file

def demo_gui_launch():
    """Demonstrate GUI application"""
    print("\n" + "="*80)
    print("🖼️  GUI APPLICATION DEMO")
    print("="*80)
    
    print("\n🚀 The GUI application provides:")
    print("   • 📁 Easy file selection and drag-drop")
    print("   • ⚡ Real-time processing with progress bars")
    print("   • 📊 Split-pane results display")
    print("   • 💾 Export options (JSON, HTML)")
    print("   • 👁️  Integrated report viewer")
    
    choice = input("\n❓ Would you like to launch the GUI application? (y/n): ").lower().strip()
    
    if choice in ['y', 'yes']:
        print("\n🎯 Launching GUI application...")
        try:
            import subprocess
            subprocess.Popen([sys.executable, "gui_app.py"])
            print("✅ GUI launched successfully!")
            print("   The application window should appear shortly.")
        except Exception as e:
            print(f"❌ Failed to launch GUI: {e}")
            print("   You can manually run: python gui_app.py")
    else:
        print("⏭️  Skipping GUI launch.")

def show_system_capabilities():
    """Show system capabilities and features"""
    print("\n" + "="*80)
    print("🔧 SYSTEM CAPABILITIES")
    print("="*80)
    
    capabilities = [
        ("📄 Document Processing", [
            "PDF documents (single/multi-page)",
            "Image files (JPG, PNG, TIFF, BMP)",
            "Text files for testing",
            "Batch processing of multiple files"
        ]),
        ("🤖 OCR Engine", [
            "Ensemble OCR approach",
            "Multi-language support (Hindi, English, Odia, Telugu, Bengali)",
            "Confidence scoring",
            "Image preprocessing and enhancement"
        ]),
        ("🧠 Named Entity Recognition", [
            "FRA-specific entity extraction",
            "Claimant information (name, tribe, location)",
            "Claim details (type, area, date)",
            "Data validation and cleaning"
        ]),
        ("📊 Output Formats", [
            "Structured JSON data",
            "Interactive HTML reports",
            "Console visualization",
            "Database storage (PostgreSQL + PostGIS)"
        ]),
        ("🎯 Performance Metrics", [
            "OCR Accuracy: ≥85% (printed), ≥70% (handwritten)",
            "NER Accuracy: ≥80% F1 score",
            "Processing Speed: ≤1 minute per document",
            "Automation Rate: ≥90% without manual review"
        ])
    ]
    
    for category, features in capabilities:
        print(f"\n{category}:")
        for feature in features:
            print(f"   ✓ {feature}")

def main():
    """Main demo function"""
    print_banner()
    
    # Check if sample file exists
    if not os.path.exists("sample_fra_claim.txt"):
        print("❌ Sample file not found. Please ensure 'sample_fra_claim.txt' exists.")
        return
    
    try:
        # Show system capabilities
        show_system_capabilities()
        
        # Demo console processing
        result = demo_console_processing()
        
        # Demo exports
        html_file = demo_html_report(result)
        json_file = demo_json_export(result)
        
        # Demo GUI
        demo_gui_launch()
        
        # Final summary
        print("\n" + "="*80)
        print("🎉 DEMO COMPLETED SUCCESSFULLY!")
        print("="*80)
        
        print(f"\n📁 Generated files:")
        print(f"   • HTML Report: {html_file}")
        print(f"   • JSON Data: {json_file}")
        
        print(f"\n🚀 Available commands:")
        print(f"   • Console processing: python ocr_ner_digitization.py --input <file> --visualize")
        print(f"   • GUI application: python gui_app.py")
        print(f"   • Batch processing: python ocr_ner_digitization.py --input <folder> --batch")
        
        print(f"\n📖 For more information, check the documentation and source code.")
        
    except Exception as e:
        print(f"\n❌ Demo failed with error: {e}")
        print("Please check that all required files are present and try again.")

if __name__ == "__main__":
    main()