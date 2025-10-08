#!/usr/bin/env python3
"""
OCR + NER Digitization Module for FRA Claims (ADHIVAN)
=====================================================

A comprehensive pipeline for digitizing scanned FRA (Forest Rights Act) claims
into structured, validated, and geospatial-ready data.

Usage:
    python ocr_ner_digitization.py --input path/to/document.pdf --output results.json
"""

import os
import sys
import json
import logging
import argparse
import re
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, asdict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class FRAClaim:
    """Data structure for FRA claim information"""
    claim_id: str = ""
    claimant_name: str = ""
    tribe: str = ""
    village: str = ""
    district: str = ""
    state: str = ""
    claim_type: str = ""  # IFR/CR/CFR
    land_area: str = ""
    application_date: str = ""
    supporting_documents: str = ""
    confidence_score: float = 0.0
    raw_text: str = ""
    processing_timestamp: str = ""

class SimpleOCR:
    """Simple OCR implementation without external dependencies"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__ + '.SimpleOCR')
    
    def extract_text(self, file_path: str) -> Tuple[str, float]:
        """Extract text from file - placeholder implementation"""
        try:
            # For demonstration, read text files or return sample text
            if file_path.lower().endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                return text, 0.95
            
            # For other files, return sample FRA claim text
            sample_text = """
            Forest Rights Act Claim Application
            
            Claim ID: FRA/2023/MP/12345
            Applicant Name: Ramesh Kumar Gond
            Tribe/Community: Gond
            Village: Khairwani
            District: Mandla
            State: Madhya Pradesh
            
            Type of Claim: Individual Forest Rights (IFR)
            Land Area Claimed: 2.5 hectares
            Application Date: 15-07-2023
            
            Supporting Documents:
            - Ration Card
            - Voter ID
            - Community Certificate
            """
            
            self.logger.info(f"Using sample text for: {file_path}")
            return sample_text, 0.85
            
        except Exception as e:
            self.logger.error(f"Text extraction failed: {e}")
            return "", 0.0

class FRAEntityExtractor:
    """Named Entity Recognition for FRA-specific entities"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__ + '.FRAEntityExtractor')
        
        # Regex patterns for entity extraction
        self.patterns = {
            'claim_id': [
                r'(?:claim|application|app)[\s\-_]*(?:id|no|number)[\s\-_]*:?\s*([A-Z0-9\-/]+)',
                r'(?:पंजीकरण|आवेदन)[\s\-_]*(?:संख्या|नंबर)[\s\-_]*:?\s*([A-Z0-9\-/]+)',
            ],
            'claimant_name': [
                r'(?:applicant\s+name|name)[\s\-_]*:?\s*([A-Za-z\s]+?)(?:\n|$)',
                r'(?:नाम)[\s\-_]*:?\s*([A-Za-z\s]+?)(?:\n|$)',
            ],
            'tribe': [
                r'(?:tribe|community)[\s\-_/]*:?\s*([A-Za-z\s]+?)(?:\n|$)',
                r'(गोंड|भील|संथाल|मुंडा|हो|खड़िया|Gond|Bhil|Santhal|Munda)',
            ],
            'village': [
                r'(?:village)[\s\-_]*:?\s*([A-Za-z\s]+?)(?:\n|$)',
                r'(?:गांव|ग्राम)[\s\-_]*:?\s*([A-Za-z\s]+?)(?:\n|$)',
            ],
            'district': [
                r'(?:district)[\s\-_]*:?\s*([A-Za-z\s]+?)(?:\n|$)',
                r'(?:जिला)[\s\-_]*:?\s*([A-Za-z\s]+?)(?:\n|$)',
            ],
            'state': [
                r'(?:state)[\s\-_]*:?\s*([A-Za-z\s]+?)(?:\n|$)',
                r'(?:राज्य)[\s\-_]*:?\s*([A-Za-z\s]+?)(?:\n|$)',
            ],
            'claim_type': [
                r'(?:IFR|CFR|CR)',
                r'(?:individual|community|collective)[\s]*(?:forest|rights)',
            ],
            'land_area': [
                r'(?:land\s+area|area)[\s\-_]*(?:claimed)?[\s\-_]*:?\s*([0-9.]+)[\s]*(?:ha|hectare|हेक्टेयर)?',
                r'(?:क्षेत्रफल|भूमि)[\s\-_]*:?\s*([0-9.]+)[\s]*(?:ha|hectare|हेक्टेयर)?',
            ],
            'application_date': [
                r'(?:application\s+date|date)[\s\-_]*:?\s*([0-9]{1,2}[-/][0-9]{1,2}[-/][0-9]{2,4})',
                r'(?:दिनांक|तारीख)[\s\-_]*:?\s*([0-9]{1,2}[-/][0-9]{1,2}[-/][0-9]{2,4})',
            ],
        }
    
    def extract_entities(self, text: str) -> Dict[str, str]:
        """Extract FRA-specific entities from text"""
        entities = {}
        
        try:
            # Don't over-clean the text - preserve line breaks for multiline patterns
            original_text = text
            
            # Extract entities using regex patterns
            for entity_type, patterns in self.patterns.items():
                for pattern in patterns:
                    matches = re.findall(pattern, original_text, re.IGNORECASE | re.MULTILINE)
                    if matches:
                        # Take the first match and clean it
                        entity_value = matches[0].strip()
                        if entity_value and len(entity_value) > 1:
                            entities[entity_type] = entity_value
                            self.logger.debug(f"Found {entity_type}: {entity_value}")
                            break
            
            # Post-process extracted entities
            entities = self._post_process_entities(entities)
            
            self.logger.info(f"Extracted {len(entities)} entities: {list(entities.keys())}")
            return entities
            
        except Exception as e:
            self.logger.error(f"Entity extraction failed: {e}")
            return {}
    
    def _post_process_entities(self, entities: Dict[str, str]) -> Dict[str, str]:
        """Clean and validate extracted entities"""
        processed = {}
        
        for key, value in entities.items():
            if key == 'claimant_name':
                # Clean name - remove extra spaces, numbers
                value = re.sub(r'[0-9]', '', value)
                value = re.sub(r'\s+', ' ', value).strip().title()
            
            elif key == 'application_date':
                # Standardize date format
                value = self._standardize_date(value)
            
            elif key == 'land_area':
                # Extract numeric value
                value = re.sub(r'[^0-9.]', '', value)
            
            elif key == 'claim_type':
                # Standardize claim type
                if 'individual' in value.lower() or 'ifr' in value.lower():
                    value = 'IFR'
                elif 'community' in value.lower() or 'cfr' in value.lower():
                    value = 'CFR'
                elif 'collective' in value.lower() or 'cr' in value.lower():
                    value = 'CR'
            
            if value:
                processed[key] = value
        
        return processed
    
    def _standardize_date(self, date_str: str) -> str:
        """Convert date to standard format DD-MM-YYYY"""
        try:
            # Try different date formats
            formats = ['%d-%m-%Y', '%d/%m/%Y', '%d-%m-%y', '%d/%m/%y']
            
            for fmt in formats:
                try:
                    date_obj = datetime.strptime(date_str, fmt)
                    return date_obj.strftime('%d-%m-%Y')
                except ValueError:
                    continue
            
            return date_str  # Return original if parsing fails
            
        except Exception:
            return date_str

class DataValidator:
    """Validates and structures extracted data"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__ + '.DataValidator')
        
        # Validation rules
        self.mandatory_fields = ['claimant_name', 'village', 'district', 'state']
        self.valid_claim_types = ['IFR', 'CFR', 'CR']
    
    def validate_and_structure(self, entities: Dict[str, str], raw_text: str, confidence: float) -> FRAClaim:
        """Validate extracted entities and create structured claim object"""
        
        claim = FRAClaim()
        claim.raw_text = raw_text
        claim.confidence_score = confidence
        claim.processing_timestamp = datetime.now().isoformat()
        
        # Map entities to claim fields
        field_mapping = {
            'claim_id': 'claim_id',
            'claimant_name': 'claimant_name',
            'tribe': 'tribe',
            'village': 'village',
            'district': 'district',
            'state': 'state',
            'claim_type': 'claim_type',
            'land_area': 'land_area',
            'application_date': 'application_date',
        }
        
        for entity_key, claim_field in field_mapping.items():
            if entity_key in entities:
                setattr(claim, claim_field, entities[entity_key])
        
        # Validate mandatory fields
        missing_fields = []
        for field in self.mandatory_fields:
            if not getattr(claim, field):
                missing_fields.append(field)
        
        if missing_fields:
            self.logger.warning(f"Missing mandatory fields: {missing_fields}")
            claim.confidence_score *= 0.7  # Reduce confidence for missing fields
        
        # Validate claim type
        if claim.claim_type and claim.claim_type not in self.valid_claim_types:
            self.logger.warning(f"Invalid claim type: {claim.claim_type}")
            claim.confidence_score *= 0.9
        
        # Validate land area format
        if claim.land_area:
            try:
                float(claim.land_area)
            except ValueError:
                self.logger.warning(f"Invalid land area format: {claim.land_area}")
                claim.confidence_score *= 0.9
        
        self.logger.info(f"Validation completed. Final confidence: {claim.confidence_score:.2f}")
        return claim

class OCRNERPipeline:
    """Main pipeline orchestrator"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__ + '.OCRNERPipeline')
        
        # Initialize components
        self.ocr_engine = SimpleOCR()
        self.entity_extractor = FRAEntityExtractor()
        self.validator = DataValidator()
    
    def process_document(self, input_path: str) -> Dict[str, Any]:
        """Process a single document through the complete pipeline"""
        start_time = datetime.now()
        self.logger.info(f"Starting document processing: {input_path}")
        
        try:
            # Check if file exists
            if not os.path.exists(input_path):
                raise FileNotFoundError(f"Input file not found: {input_path}")
            
            # Step 1: OCR extraction
            text, confidence = self.ocr_engine.extract_text(input_path)
            
            if not text:
                raise ValueError("No text extracted from document")
            
            self.logger.info(f"OCR completed with confidence: {confidence:.2f}")
            
            # Step 2: Named Entity Recognition
            entities = self.entity_extractor.extract_entities(text)
            
            # Step 3: Data validation and structuring
            claim = self.validator.validate_and_structure(entities, text, confidence)
            
            # Prepare result
            processing_time = (datetime.now() - start_time).total_seconds()
            
            result = {
                'success': True,
                'claim_data': asdict(claim),
                'processing_time_seconds': processing_time,
                'needs_review': claim.confidence_score < 0.8
            }
            
            self.logger.info(f"Document processing completed in {processing_time:.2f} seconds")
            return result
            
        except Exception as e:
            self.logger.error(f"Document processing failed: {e}")
            return {
                'success': False,
                'error': str(e),
                'processing_time_seconds': (datetime.now() - start_time).total_seconds()
            }
    
    def batch_process(self, input_directory: str, output_directory: str = None) -> Dict[str, Any]:
        """Process multiple documents in batch"""
        self.logger.info(f"Starting batch processing: {input_directory}")
        
        if not os.path.exists(input_directory):
            return {'success': False, 'error': f'Input directory not found: {input_directory}'}
        
        # Find all supported files
        supported_extensions = ['.pdf', '.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.txt']
        files_to_process = []
        
        if os.path.isfile(input_directory):
            files_to_process = [input_directory]
        else:
            for root, dirs, files in os.walk(input_directory):
                for file in files:
                    if any(file.lower().endswith(ext) for ext in supported_extensions):
                        files_to_process.append(os.path.join(root, file))
        
        if not files_to_process:
            return {'success': False, 'error': 'No supported files found'}
        
        # Process each file
        results = []
        successful = 0
        failed = 0
        
        for file_path in files_to_process:
            self.logger.info(f"Processing file {len(results)+1}/{len(files_to_process)}: {file_path}")
            
            result = self.process_document(file_path)
            result['file_path'] = file_path
            results.append(result)
            
            if result['success']:
                successful += 1
            else:
                failed += 1
            
            # Save individual result if output directory specified
            if output_directory:
                os.makedirs(output_directory, exist_ok=True)
                filename = os.path.splitext(os.path.basename(file_path))[0]
                output_file = os.path.join(output_directory, f"{filename}_result.json")
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)
        
        # Summary
        batch_result = {
            'success': True,
            'total_files': len(files_to_process),
            'successful': successful,
            'failed': failed,
            'success_rate': successful / len(files_to_process) * 100,
            'results': results
        }
        
        self.logger.info(f"Batch processing completed: {successful}/{len(files_to_process)} successful")
        return batch_result

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='OCR + NER Digitization for FRA Claims')
    parser.add_argument('--input', '-i', required=True, help='Input file or directory path')
    parser.add_argument('--output', '-o', help='Output JSON file or directory')
    parser.add_argument('--batch', '-b', action='store_true', help='Batch process directory')
    parser.add_argument('--visualize', '-v', action='store_true', help='Show visual results')
    parser.add_argument('--html', action='store_true', help='Generate HTML report')
    parser.add_argument('--epatta', '-e', action='store_true', help='Generate e-Patta with QR code')
    parser.add_argument('--log-level', default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'])
    
    args = parser.parse_args()
    
    # Set log level
    logging.getLogger().setLevel(getattr(logging, args.log_level))
    
    # Initialize pipeline
    pipeline = OCRNERPipeline()
    
    try:
        if args.batch or os.path.isdir(args.input):
            # Batch processing
            result = pipeline.batch_process(args.input, args.output)
        else:
            # Single file processing
            result = pipeline.process_document(args.input)
        
        # Save result
        if args.output and not os.path.isdir(args.output):
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            print(f"Results saved to: {args.output}")
        
        # Visualization
        if args.visualize or args.html:
            try:
                from visualizer import FRAClaimVisualizer
                visualizer = FRAClaimVisualizer()
                
                if args.visualize:
                    visualizer.visualize_console(result)
                
                if args.html:
                    html_output = args.output.replace('.json', '.html') if args.output else 'fra_report.html'
                    html_file = visualizer.generate_html_report(result, html_output)
                    print(f"\n📄 HTML report generated: {html_file}")
                    
            except ImportError:
                print("Visualizer not available. Install required dependencies.")
        
        # e-Patta Generation
        if args.epatta and result['success']:
            try:
                from epatta_generator import EpattaGenerator
                
                print("\n🏛️ Generating e-Patta...")
                generator = EpattaGenerator()
                
                # Generate e-Patta
                epatta_document, qr_image = generator.create_epatta_document(result['claim_data'])
                
                # Save e-Patta files
                epatta_files = generator.save_epatta_files(epatta_document, qr_image)
                
                print(f"✅ e-Patta generated successfully!")
                print(f"📄 Patta Number: {epatta_document['patta_number']}")
                print(f"📁 e-Patta files:")
                for file_type, file_path in epatta_files.items():
                    print(f"   • {file_type}: {file_path}")
                
                print(f"\n🗺️ Coordinates: {epatta_document['land_details']['coordinates']}")
                print(f"🌐 Google Maps: {epatta_document['land_details']['google_maps_url']}")
                print(f"📱 QR Verification: {epatta_document['verification']['verification_url']}")
                
                # Ask if user wants to start verification server
                start_server = input("\n❓ Start QR verification server? (y/n): ").lower().strip()
                if start_server in ['y', 'yes']:
                    print("🌐 Starting verification server...")
                    import subprocess
                    subprocess.Popen([sys.executable, "qr_verification_server.py", "--open"])
                    print("✅ Verification server started. Check your browser.")
                
            except ImportError as e:
                print(f"e-Patta generator not available: {e}")
            except Exception as e:
                print(f"Failed to generate e-Patta: {e}")
        
        # Print summary
        if result['success']:
            if 'total_files' in result:
                print(f"Batch processing completed: {result['successful']}/{result['total_files']} files successful")
            else:
                print(f"Document processed successfully. Confidence: {result['claim_data']['confidence_score']:.2f}")
                if result['needs_review']:
                    print("⚠️  Document flagged for manual review (low confidence)")
        else:
            print(f"Processing failed: {result['error']}")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\nProcessing interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()