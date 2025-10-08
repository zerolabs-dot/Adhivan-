#!/usr/bin/env python3
"""
GUI Application for FRA Claim Digitization
==========================================

A user-friendly GUI interface for the OCR + NER pipeline with:
- File selection and drag-drop
- Real-time processing visualization
- Separate output space for results
- Export options (JSON, HTML, PDF)
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import json
import os
import threading
from datetime import datetime
from typing import Dict, Any
import webbrowser

# Import our pipeline modules
from ocr_ner_digitization import OCRNERPipeline
from visualizer import FRAClaimVisualizer

class FRAClaimGUI:
    """Main GUI application for FRA claim processing"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Government of India - Forest Rights Act | Digital Claim Processing System")
        self.root.geometry("1400x900")
        self.root.configure(bg='#FAFAFA')
        self.root.state('zoomed')  # Maximize window on Windows
        
        # Initialize components
        self.pipeline = OCRNERPipeline()
        self.visualizer = FRAClaimVisualizer()
        self.current_result = None
        
        # Setup GUI
        self.setup_styles()
        self.create_widgets()
        self.setup_layout()
        
    def setup_styles(self):
        """Configure professional government styles"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Government color scheme - Professional and formal
        self.colors = {
            'primary': '#1565C0',      # Government blue
            'secondary': '#0D47A1',    # Dark blue
            'accent': '#1976D2',       # Medium blue
            'background': '#FAFAFA',   # Light gray
            'surface': '#FFFFFF',      # White
            'text': '#212121',         # Dark gray
            'text_secondary': '#757575', # Medium gray
            'error': '#C62828',        # Red
            'warning': '#F57C00',      # Orange
            'success': '#2E7D32',      # Green
            'border': '#E0E0E0'        # Light border
        }
        
        # Configure professional styles
        self.style.configure('Title.TLabel', 
                           font=('Segoe UI', 18, 'bold'),
                           foreground=self.colors['primary'],
                           background=self.colors['background'])
        
        self.style.configure('Header.TLabel',
                           font=('Segoe UI', 11, 'bold'),
                           foreground=self.colors['text'],
                           background=self.colors['background'])
        
        self.style.configure('Subheader.TLabel',
                           font=('Segoe UI', 10, 'bold'),
                           foreground=self.colors['text_secondary'],
                           background=self.colors['background'])
        
        self.style.configure('Body.TLabel',
                           font=('Segoe UI', 9),
                           foreground=self.colors['text'],
                           background=self.colors['background'])
        
        self.style.configure('Success.TLabel',
                           font=('Segoe UI', 9, 'bold'),
                           foreground=self.colors['success'],
                           background=self.colors['background'])
        
        self.style.configure('Error.TLabel',
                           font=('Segoe UI', 9, 'bold'),
                           foreground=self.colors['error'],
                           background=self.colors['background'])
        
        self.style.configure('Warning.TLabel',
                           font=('Segoe UI', 9, 'bold'),
                           foreground=self.colors['warning'],
                           background=self.colors['background'])
        
        # Button styles
        self.style.configure('Primary.TButton',
                           font=('Segoe UI', 9, 'bold'),
                           foreground='white',
                           background=self.colors['primary'],
                           borderwidth=0,
                           focuscolor='none')
        
        self.style.map('Primary.TButton',
                      background=[('active', self.colors['accent']),
                                ('pressed', self.colors['secondary'])])
        
        self.style.configure('Secondary.TButton',
                           font=('Segoe UI', 9),
                           foreground=self.colors['primary'],
                           background=self.colors['surface'],
                           borderwidth=1,
                           focuscolor='none')
        
        # Configure root window background
        self.root.configure(bg=self.colors['background'])
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Main container
        self.main_frame = ttk.Frame(self.root, padding="10")
        
        # Government Header
        self.header_frame = ttk.Frame(self.main_frame)
        
        # Government emblem and title
        self.title_label = ttk.Label(self.header_frame, 
                                   text="भारत सरकार | Government of India",
                                   style='Title.TLabel')
        
        self.subtitle_label = ttk.Label(self.header_frame,
                                      text="Ministry of Tribal Affairs | Forest Rights Act Implementation",
                                      style='Header.TLabel')
        
        self.system_label = ttk.Label(self.header_frame,
                                    text="Digital Claim Processing & e-Patta Generation System",
                                    style='Subheader.TLabel')
        
        # Input section
        self.input_frame = ttk.LabelFrame(self.main_frame, text="Document Upload & Processing", 
                                        padding="15")
        
        # File selection with professional styling
        self.file_label = ttk.Label(self.input_frame, text="Select FRA Claim Document:", style='Body.TLabel')
        
        self.file_path_var = tk.StringVar()
        self.file_entry = ttk.Entry(self.input_frame, textvariable=self.file_path_var, 
                                  width=70)
        
        self.browse_button = ttk.Button(self.input_frame, text="Browse Documents", 
                                      command=self.browse_files, style='Secondary.TButton')
        
        self.process_button = ttk.Button(self.input_frame, text="Process & Generate e-Patta", 
                                       command=self.process_document, style='Primary.TButton')
        
        # Progress section
        self.progress_frame = ttk.LabelFrame(self.main_frame, text="Processing Status & System Information", 
                                           padding="15")
        
        self.progress_var = tk.StringVar(value="Ready to process documents...")
        self.progress_label = ttk.Label(self.progress_frame, textvariable=self.progress_var)
        self.progress_bar = ttk.Progressbar(self.progress_frame, mode='indeterminate')
        
        # Results section - Split into two panes
        self.results_frame = ttk.LabelFrame(self.main_frame, text="Claim Processing Results & Document Analysis", 
                                          padding="15")
        
        # Create paned window for split view
        self.paned_window = ttk.PanedWindow(self.results_frame, orient=tk.HORIZONTAL)
        
        # Left pane - Extracted data
        self.data_frame = ttk.Frame(self.paned_window)
        self.data_label = ttk.Label(self.data_frame, text="Extracted Claim Information", style='Header.TLabel')
        
        # Scrollable frame for extracted data
        self.data_canvas = tk.Canvas(self.data_frame, bg='white', height=300)
        self.data_scrollbar = ttk.Scrollbar(self.data_frame, orient="vertical", command=self.data_canvas.yview)
        self.data_canvas.configure(yscrollcommand=self.data_scrollbar.set)
        
        self.data_content_frame = ttk.Frame(self.data_canvas)
        self.data_canvas.create_window((0, 0), window=self.data_content_frame, anchor="nw")
        
        # Right pane - Raw text and analysis
        self.analysis_frame = ttk.Frame(self.paned_window)
        self.analysis_label = ttk.Label(self.analysis_frame, text="Document Analysis & Verification", style='Header.TLabel')
        
        self.raw_text_area = scrolledtext.ScrolledText(self.analysis_frame, 
                                                     width=50, height=15,
                                                     wrap=tk.WORD, font=('Courier', 9))
        
        # Confidence and status display
        self.status_frame = ttk.Frame(self.analysis_frame)
        self.confidence_var = tk.StringVar(value="Confidence: --")
        self.confidence_label = ttk.Label(self.status_frame, textvariable=self.confidence_var)
        
        self.status_var = tk.StringVar(value="Status: Ready")
        self.status_label = ttk.Label(self.status_frame, textvariable=self.status_var)
        
        # Export section
        self.export_frame = ttk.LabelFrame(self.main_frame, text="Document Generation & Export Options", 
                                         padding="15")
        
        self.export_json_button = ttk.Button(self.export_frame, text="Export Data (JSON)", 
                                           command=self.export_json, style='Secondary.TButton')
        self.export_html_button = ttk.Button(self.export_frame, text="Generate Report (HTML)", 
                                           command=self.export_html, style='Secondary.TButton')
        self.generate_epatta_button = ttk.Button(self.export_frame, text="Generate Official e-Patta", 
                                               command=self.generate_epatta, style='Primary.TButton')
        self.view_html_button = ttk.Button(self.export_frame, text="View Processing Report", 
                                         command=self.view_html_report, style='Secondary.TButton')
        
        # Add panes to paned window
        self.paned_window.add(self.data_frame, weight=1)
        self.paned_window.add(self.analysis_frame, weight=1)
        
        # Initialize data display
        self.create_data_fields()
    
    def setup_layout(self):
        """Arrange widgets in the layout"""
        # Main frame
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        
        # Header section
        self.header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 25))
        self.header_frame.columnconfigure(0, weight=1)
        
        self.title_label.grid(row=0, column=0, pady=(0, 5))
        self.subtitle_label.grid(row=1, column=0, pady=(0, 3))
        self.system_label.grid(row=2, column=0, pady=(0, 10))
        
        # Input section
        self.input_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        self.input_frame.columnconfigure(1, weight=1)
        
        self.file_label.grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=(0, 8))
        self.file_entry.grid(row=1, column=0, padx=(0, 10), sticky=(tk.W, tk.E))
        self.browse_button.grid(row=1, column=1, padx=(0, 15))
        self.process_button.grid(row=1, column=2)
        
        # Progress section
        self.progress_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        self.progress_frame.columnconfigure(0, weight=1)
        
        self.progress_label.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 8))
        self.progress_bar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Results section
        self.results_frame.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 15))
        self.results_frame.columnconfigure(0, weight=1)
        self.results_frame.rowconfigure(0, weight=1)
        
        self.paned_window.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        
        # Left pane layout
        self.data_frame.columnconfigure(0, weight=1)
        self.data_frame.rowconfigure(1, weight=1)
        
        self.data_label.grid(row=0, column=0, pady=(5, 15), sticky=tk.W)
        self.data_canvas.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.data_scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        
        # Right pane layout
        self.analysis_frame.columnconfigure(0, weight=1)
        self.analysis_frame.rowconfigure(1, weight=1)
        
        self.analysis_label.grid(row=0, column=0, pady=(5, 15), sticky=tk.W)
        self.raw_text_area.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.status_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(15, 0))
        self.status_frame.columnconfigure(0, weight=1)
        self.status_frame.columnconfigure(1, weight=1)
        
        self.confidence_label.grid(row=0, column=0, sticky=tk.W)
        self.status_label.grid(row=0, column=1, sticky=tk.E)
        
        # Export section
        self.export_frame.grid(row=4, column=0, sticky=(tk.W, tk.E))
        
        self.export_json_button.grid(row=0, column=0, padx=(0, 15), pady=5)
        self.export_html_button.grid(row=0, column=1, padx=(0, 15), pady=5)
        self.generate_epatta_button.grid(row=0, column=2, padx=(0, 15), pady=5)
        self.view_html_button.grid(row=0, column=3, pady=5)
        
        # Configure main frame row weights
        self.main_frame.rowconfigure(3, weight=1)
    
    def create_data_fields(self):
        """Create fields for displaying extracted data"""
        self.data_fields = {}
        
        fields = [
            ('Claim/Application ID', 'claim_id'),
            ('Claimant Full Name', 'claimant_name'),
            ('Tribe/Community', 'tribe'),
            ('Village', 'village'),
            ('District', 'district'),
            ('State/UT', 'state'),
            ('Claim Type', 'claim_type'),
            ('Land Area (Hectares)', 'land_area'),
            ('Application Date', 'application_date'),
        ]
        
        for i, (display_name, field_key) in enumerate(fields):
            # Create a frame for each field
            field_frame = ttk.Frame(self.data_content_frame)
            field_frame.grid(row=i, column=0, sticky=(tk.W, tk.E), pady=8, padx=10)
            field_frame.columnconfigure(1, weight=1)
            
            # Label
            label = ttk.Label(field_frame, text=f"{display_name}:", 
                            font=('Segoe UI', 9, 'bold'), 
                            foreground=self.colors['text'])
            label.grid(row=0, column=0, sticky=tk.W, padx=(0, 15))
            
            # Value
            value_var = tk.StringVar(value="Awaiting document processing...")
            value_label = ttk.Label(field_frame, textvariable=value_var,
                                  font=('Segoe UI', 9), 
                                  foreground=self.colors['text_secondary'])
            value_label.grid(row=0, column=1, sticky=tk.W)
            
            self.data_fields[field_key] = value_var
        
        # Update scroll region
        self.data_content_frame.update_idletasks()
        self.data_canvas.configure(scrollregion=self.data_canvas.bbox("all"))
    
    def browse_files(self):
        """Open file browser to select input file"""
        filetypes = [
            ('All Supported', '*.pdf;*.jpg;*.jpeg;*.png;*.tiff;*.bmp;*.txt'),
            ('PDF files', '*.pdf'),
            ('Image files', '*.jpg;*.jpeg;*.png;*.tiff;*.bmp'),
            ('Text files', '*.txt'),
            ('All files', '*.*')
        ]
        
        filename = filedialog.askopenfilename(
            title="Select FRA Claim Document",
            filetypes=filetypes
        )
        
        if filename:
            self.file_path_var.set(filename)
    
    def process_document(self):
        """Process the selected document"""
        file_path = self.file_path_var.get().strip()
        
        if not file_path:
            messagebox.showerror("Error", "Please select a file to process")
            return
        
        if not os.path.exists(file_path):
            messagebox.showerror("Error", f"File not found: {file_path}")
            return
        
        # Disable process button and start progress
        self.process_button.configure(state='disabled')
        self.progress_bar.start()
        self.progress_var.set("Processing document...")
        
        # Run processing in separate thread
        thread = threading.Thread(target=self._process_thread, args=(file_path,))
        thread.daemon = True
        thread.start()
    
    def _process_thread(self, file_path):
        """Process document in separate thread"""
        try:
            # Process the document
            result = self.pipeline.process_document(file_path)
            
            # Update GUI in main thread
            self.root.after(0, self._update_results, result)
            
        except Exception as e:
            error_result = {
                'success': False,
                'error': str(e),
                'processing_time_seconds': 0
            }
            self.root.after(0, self._update_results, error_result)
    
    def _update_results(self, result):
        """Update GUI with processing results"""
        # Stop progress bar and re-enable button
        self.progress_bar.stop()
        self.process_button.configure(state='normal')
        
        self.current_result = result
        
        if result['success']:
            self.progress_var.set("✅ Processing completed successfully!")
            
            claim_data = result['claim_data']
            
            # Update data fields
            for field_key, var in self.data_fields.items():
                value = claim_data.get(field_key, '')
                if value:
                    var.set(value)
                else:
                    var.set("Not found")
            
            # Update raw text
            raw_text = claim_data.get('raw_text', '')
            self.raw_text_area.delete(1.0, tk.END)
            self.raw_text_area.insert(1.0, raw_text)
            
            # Update confidence and status
            confidence = claim_data.get('confidence_score', 0)
            self.confidence_var.set(f"Confidence: {confidence:.2f} ({confidence*100:.1f}%)")
            
            if result.get('needs_review', False):
                self.status_var.set("Status: ⚠️ Needs Review")
                self.status_label.configure(style='Error.TLabel')
            else:
                self.status_var.set("Status: ✅ Auto-Approved")
                self.status_label.configure(style='Success.TLabel')
            
        else:
            self.progress_var.set(f"❌ Processing failed: {result.get('error', 'Unknown error')}")
            
            # Clear fields
            for var in self.data_fields.values():
                var.set("Processing failed")
            
            self.raw_text_area.delete(1.0, tk.END)
            self.raw_text_area.insert(1.0, f"Error: {result.get('error', 'Unknown error')}")
            
            self.confidence_var.set("Confidence: --")
            self.status_var.set("Status: ❌ Failed")
            self.status_label.configure(style='Error.TLabel')
    
    def export_json(self):
        """Export results as JSON"""
        if not self.current_result:
            messagebox.showwarning("Warning", "No results to export")
            return
        
        filename = filedialog.asksaveasfilename(
            title="Save JSON Report",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(self.current_result, f, indent=2, ensure_ascii=False)
                messagebox.showinfo("Success", f"JSON report saved to:\n{filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save JSON: {e}")
    
    def export_html(self):
        """Export results as HTML"""
        if not self.current_result:
            messagebox.showwarning("Warning", "No results to export")
            return
        
        filename = filedialog.asksaveasfilename(
            title="Save HTML Report",
            defaultextension=".html",
            filetypes=[("HTML files", "*.html"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                self.visualizer.generate_html_report(self.current_result, filename)
                messagebox.showinfo("Success", f"HTML report saved to:\n{filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save HTML: {e}")
    
    def generate_epatta(self):
        """Generate e-Patta with QR code"""
        if not self.current_result or not self.current_result.get('success'):
            messagebox.showwarning("Warning", "No valid results to generate e-Patta")
            return
        
        try:
            from epatta_generator import EpattaGenerator
            
            # Show progress
            progress_window = tk.Toplevel(self.root)
            progress_window.title("Generating e-Patta")
            progress_window.geometry("400x150")
            progress_window.transient(self.root)
            progress_window.grab_set()
            
            ttk.Label(progress_window, text="🏛️ Generating e-Patta...", 
                     font=('Arial', 12)).pack(pady=20)
            
            progress = ttk.Progressbar(progress_window, mode='indeterminate')
            progress.pack(pady=10, padx=20, fill='x')
            progress.start()
            
            def generate_in_thread():
                try:
                    generator = EpattaGenerator()
                    
                    # Generate e-Patta
                    epatta_document, qr_image = generator.create_epatta_document(
                        self.current_result['claim_data']
                    )
                    
                    # Save files
                    epatta_files = generator.save_epatta_files(epatta_document, qr_image)
                    
                    # Update GUI in main thread
                    self.root.after(0, lambda: self._epatta_generated(
                        progress_window, epatta_document, epatta_files
                    ))
                    
                except Exception as e:
                    self.root.after(0, lambda: self._epatta_error(progress_window, str(e)))
            
            # Start generation in separate thread
            thread = threading.Thread(target=generate_in_thread)
            thread.daemon = True
            thread.start()
            
        except ImportError:
            messagebox.showerror("Error", "e-Patta generator not available. Please install required dependencies.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate e-Patta: {e}")
    
    def _epatta_generated(self, progress_window, epatta_document, epatta_files):
        """Handle successful e-Patta generation"""
        progress_window.destroy()
        
        # Show success dialog
        result_text = f"""e-Patta Generated Successfully!

Patta Number: {epatta_document['patta_number']}

Files Generated:
• HTML Document: {epatta_files['html_file']}
• QR Code: {epatta_files['qr_file']}
• JSON Data: {epatta_files['json_file']}

Coordinates: {epatta_document['land_details']['coordinates']}
Google Maps: {epatta_document['land_details']['google_maps_url']}
"""
        
        messagebox.showinfo("e-Patta Generated", result_text)
        
        # Ask if user wants to view the e-Patta
        if messagebox.askyesno("View e-Patta", "Would you like to view the generated e-Patta?"):
            webbrowser.open(f"file://{os.path.abspath(epatta_files['html_file'])}")
        
        # Ask if user wants to start verification server
        if messagebox.askyesno("Start Server", "Would you like to start the QR verification server?"):
            try:
                import subprocess
                subprocess.Popen([sys.executable, "qr_verification_server.py", "--open"])
                messagebox.showinfo("Server Started", "QR verification server started. Check your browser.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to start server: {e}")
    
    def _epatta_error(self, progress_window, error_message):
        """Handle e-Patta generation error"""
        progress_window.destroy()
        messagebox.showerror("e-Patta Generation Failed", f"Error: {error_message}")
    
    def view_html_report(self):
        """Generate and view HTML report in browser"""
        if not self.current_result:
            messagebox.showwarning("Warning", "No results to view")
            return
        
        try:
            # Generate temporary HTML file
            temp_filename = "temp_fra_report.html"
            self.visualizer.generate_html_report(self.current_result, temp_filename)
            
            # Open in browser
            webbrowser.open(f"file://{os.path.abspath(temp_filename)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate HTML report: {e}")

def main():
    """Main function to run the GUI application"""
    root = tk.Tk()
    app = FRAClaimGUI(root)
    
    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()

if __name__ == "__main__":
    main()