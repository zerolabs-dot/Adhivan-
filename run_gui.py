#!/usr/bin/env python3
"""
Simple launcher for the FRA Claim Digitization GUI
==================================================

This script launches the GUI application with proper error handling
and dependency checking.
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox

def check_dependencies():
    """Check if required modules are available"""
    missing = []
    
    try:
        import tkinter
    except ImportError:
        missing.append("tkinter")
    
    # Check if our modules exist
    if not os.path.exists("ocr_ner_digitization.py"):
        missing.append("ocr_ner_digitization.py")
    
    if not os.path.exists("visualizer.py"):
        missing.append("visualizer.py")
    
    if not os.path.exists("gui_app.py"):
        missing.append("gui_app.py")
    
    return missing

def main():
    """Main launcher function"""
    print("🚀 Starting FRA Claim Digitization GUI...")
    
    # Check dependencies
    missing = check_dependencies()
    if missing:
        print(f"❌ Missing dependencies: {', '.join(missing)}")
        print("Please ensure all required files are in the same directory.")
        input("Press Enter to exit...")
        return
    
    try:
        # Import and run the GUI
        from gui_app import main as run_gui
        print("✅ All dependencies found. Launching GUI...")
        run_gui()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please check that all required Python packages are installed.")
        input("Press Enter to exit...")
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        
        # Show error in GUI if possible
        try:
            root = tk.Tk()
            root.withdraw()  # Hide main window
            messagebox.showerror("Error", f"Failed to start application:\n{e}")
            root.destroy()
        except:
            pass
        
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()