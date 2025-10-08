#!/usr/bin/env python3
"""
Main Application Launcher for FRA Claim Digitization System
==========================================================

Integrated workflow:
1. GUI for document upload and processing
2. Automatic OCR + NER processing
3. Automatic e-Patta generation with QR codes
4. Automatic QR verification server launch
5. Seamless flow from verification to processing

Usage:
    python main_app.py
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox
import threading
import subprocess
import time
import webbrowser
from datetime import datetime

class FRAMainApplication:
    """Main application controller for the complete FRA workflow"""
    
    def __init__(self):
        self.verification_server_process = None
        self.gui_app = None
        
    def check_dependencies(self):
        """Check if all required modules are available"""
        missing = []
        required_files = [
            "gui_app.py",
            "ocr_ner_digitization.py", 
            "epatta_generator.py",
            "qr_verification_server.py",
            "visualizer.py"
        ]
        
        for file in required_files:
            if not os.path.exists(file):
                missing.append(file)
        
        # Check Python modules
        try:
            import tkinter
            import PIL
            import qrcode
        except ImportError as e:
            missing.append(f"Python module: {e}")
        
        return missing
    
    def start_verification_server(self, port=8080):
        """Start the QR verification server in background"""
        try:
            if self.verification_server_process and self.verification_server_process.poll() is None:
                print("🌐 Verification server already running")
                return True
            
            print(f"🌐 Starting QR verification server on port {port}...")
            
            # Start server process
            self.verification_server_process = subprocess.Popen([
                sys.executable, "qr_verification_server.py", 
                "--port", str(port)
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Wait a moment for server to start
            time.sleep(2)
            
            # Check if server started successfully
            if self.verification_server_process.poll() is None:
                print(f"✅ Verification server started successfully on http://localhost:{port}")
                return True
            else:
                print("❌ Failed to start verification server")
                return False
                
        except Exception as e:
            print(f"❌ Error starting verification server: {e}")
            return False
    
    def launch_gui_with_integration(self):
        """Launch GUI with enhanced integration features"""
        try:
            # Import GUI components
            from gui_app import FRAClaimGUI
            
            # Create root window
            root = tk.Tk()
            
            # Create enhanced GUI with auto-flow features
            gui = EnhancedFRAGUI(root, self)
            self.gui_app = gui
            
            # Start the GUI
            root.mainloop()
            
        except Exception as e:
            print(f"❌ Failed to launch GUI: {e}")
            messagebox.showerror("Error", f"Failed to launch GUI: {e}")
    
    def cleanup(self):
        """Clean up resources when application closes"""
        if self.verification_server_process:
            try:
                self.verification_server_process.terminate()
                print("🛑 Verification server stopped")
            except:
                pass
    
    def run(self):
        """Main application entry point"""
        print("🚀 Starting FRA Claim Digitization System...")
        print("=" * 60)
        
        # Check dependencies
        missing = self.check_dependencies()
        if missing:
            print("❌ Missing dependencies:")
            for item in missing:
                print(f"   • {item}")
            print("\nPlease ensure all required files and modules are available.")
            input("Press Enter to exit...")
            return
        
        print("✅ All dependencies found")
        
        # Start verification server in background
        server_started = self.start_verification_server()
        
        # Launch GUI
        print("🖥️ Launching GUI application...")
        try:
            self.launch_gui_with_integration()
        finally:
            self.cleanup()

class EnhancedFRAGUI:
    """Enhanced GUI with automatic workflow integration"""
    
    def __init__(self, root, main_app):
        self.root = root
        self.main_app = main_app
        
        # Import and setup base GUI
        from gui_app import FRAClaimGUI
        self.base_gui = FRAClaimGUI(root)
        
        # Override process_document method for auto-flow
        self.base_gui.process_document = self.enhanced_process_document
        
        # Add auto-flow status
        self.auto_flow_enabled = tk.BooleanVar(value=True)
        self.add_auto_flow_controls()
    
    def add_auto_flow_controls(self):
        """Add controls for automatic workflow"""
        # Add auto-flow checkbox to the GUI
        auto_flow_frame = tk.Frame(self.base_gui.input_frame)
        auto_flow_frame.grid(row=2, column=0, columnspan=3, sticky='w', pady=(10, 0))
        
        auto_flow_check = tk.Checkbutton(
            auto_flow_frame,
            text="🔄 Enable Auto-Flow (OCR → e-Patta → Verification)",
            variable=self.auto_flow_enabled,
            font=('Segoe UI', 9),
            fg='#2E7D32'
        )
        auto_flow_check.pack(side='left')
        
        # Add status indicator
        self.flow_status_var = tk.StringVar(value="Auto-flow ready")
        status_label = tk.Label(
            auto_flow_frame,
            textvariable=self.flow_status_var,
            font=('Segoe UI', 8),
            fg='#666'
        )
        status_label.pack(side='left', padx=(20, 0))
    
    def enhanced_process_document(self):
        """Enhanced document processing with automatic workflow"""
        file_path = self.base_gui.file_path_var.get().strip()
        
        if not file_path:
            messagebox.showerror("Error", "Please select a file to process")
            return
        
        if not os.path.exists(file_path):
            messagebox.showerror("Error", f"File not found: {file_path}")
            return
        
        # Disable process button and start progress
        self.base_gui.process_button.configure(state='disabled')
        self.base_gui.progress_bar.start()
        
        if self.auto_flow_enabled.get():
            self.flow_status_var.set("🔄 Auto-flow active")
            self.base_gui.progress_var.set("🔄 Starting automatic workflow...")
            
            # Run enhanced processing in separate thread
            thread = threading.Thread(target=self._enhanced_process_thread, args=(file_path,))
            thread.daemon = True
            thread.start()
        else:
            # Use original processing
            self.flow_status_var.set("Manual processing")
            thread = threading.Thread(target=self.base_gui._process_thread, args=(file_path,))
            thread.daemon = True
            thread.start()
    
    def _enhanced_process_thread(self, file_path):
        """Enhanced processing thread with automatic workflow"""
        try:
            # Step 1: OCR + NER Processing
            self.root.after(0, lambda: self.base_gui.progress_var.set("📄 Step 1/3: Processing document with OCR + NER..."))
            
            result = self.base_gui.pipeline.process_document(file_path)
            
            if not result['success']:
                self.root.after(0, self._update_results, result)
                return
            
            # Step 2: Automatic e-Patta Generation
            self.root.after(0, lambda: self.base_gui.progress_var.set("🏛️ Step 2/3: Generating e-Patta with QR code..."))
            
            epatta_result = self._generate_epatta_auto(result['claim_data'])
            
            if epatta_result['success']:
                result['epatta_data'] = epatta_result['epatta_data']
                result['epatta_files'] = epatta_result['epatta_files']
                
                # Step 3: Verification Setup
                self.root.after(0, lambda: self.base_gui.progress_var.set("🌐 Step 3/3: Setting up verification system..."))
                
                # Ensure verification server is running
                if not self._ensure_verification_server():
                    print("⚠️ Warning: Verification server not available")
                
                # Auto-open verification page
                verification_url = epatta_result['epatta_data']['verification']['verification_url']
                
                def open_verification():
                    time.sleep(1)  # Brief delay
                    webbrowser.open(verification_url)
                
                threading.Thread(target=open_verification, daemon=True).start()
                
                result['auto_flow_completed'] = True
                result['verification_url'] = verification_url
            
            # Update GUI with final results
            self.root.after(0, self._update_enhanced_results, result)
            
        except Exception as e:
            error_result = {
                'success': False,
                'error': str(e),
                'processing_time_seconds': 0
            }
            self.root.after(0, self._update_results, error_result)
    
    def _generate_epatta_auto(self, claim_data):
        """Automatically generate e-Patta"""
        try:
            from epatta_generator import EpattaGenerator
            
            generator = EpattaGenerator()
            
            # Generate e-Patta
            epatta_document, qr_image = generator.create_epatta_document(claim_data)
            
            # Save files
            epatta_files = generator.save_epatta_files(epatta_document, qr_image)
            
            return {
                'success': True,
                'epatta_data': epatta_document,
                'epatta_files': epatta_files
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _ensure_verification_server(self):
        """Ensure verification server is running"""
        try:
            import requests
            response = requests.get("http://localhost:8080", timeout=2)
            return True
        except:
            # Try to start server if not running
            return self.main_app.start_verification_server()
    
    def _update_enhanced_results(self, result):
        """Update GUI with enhanced results"""
        # Use base GUI update method first
        self.base_gui._update_results(result)
        
        if result['success'] and result.get('auto_flow_completed'):
            # Show enhanced success message
            self.flow_status_var.set("✅ Auto-flow completed successfully!")
            
            # Update progress with completion info
            completion_msg = "✅ Workflow completed successfully!\n"
            
            if 'epatta_data' in result:
                patta_number = result['epatta_data']['patta_number']
                completion_msg += f"📄 e-Patta generated: {patta_number}\n"
            
            if 'verification_url' in result:
                completion_msg += f"🌐 Verification page opened in browser\n"
            
            completion_msg += "🔄 Ready for next document"
            
            self.base_gui.progress_var.set(completion_msg)
            
            # Show completion dialog
            self._show_completion_dialog(result)
        else:
            self.flow_status_var.set("❌ Auto-flow failed")
    
    def _show_completion_dialog(self, result):
        """Show workflow completion dialog"""
        if 'epatta_data' in result:
            patta_number = result['epatta_data']['patta_number']
            verification_url = result.get('verification_url', '')
            
            completion_text = f"""🎉 Automatic Workflow Completed Successfully!

📄 Document processed with OCR + NER
🏛️ e-Patta generated: {patta_number}
📱 QR code created for mobile verification
🌐 Verification server is running
🔗 Verification page opened in browser

The complete workflow is now ready:
• Citizens can scan QR codes to verify e-Patta
• Verification server is running at http://localhost:8080
• All files saved in epatta_output/ directory

Ready to process the next document!"""
            
            messagebox.showinfo("Workflow Complete", completion_text)
    
    def _update_results(self, result):
        """Fallback to base GUI update for errors"""
        self.base_gui._update_results(result)
        self.flow_status_var.set("❌ Processing failed")

def main():
    """Main entry point"""
    try:
        app = FRAMainApplication()
        app.run()
    except KeyboardInterrupt:
        print("\n🛑 Application interrupted by user")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        messagebox.showerror("Error", f"Application failed to start: {e}")

if __name__ == "__main__":
    main()