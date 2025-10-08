#!/usr/bin/env python3
"""
GUI Visualizer for FRA Claim Processing Results
===============================================

Creates a graphical user interface to display OCR + NER results
in a separate window with interactive elements.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
from datetime import datetime
im