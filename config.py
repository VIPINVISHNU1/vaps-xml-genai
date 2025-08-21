"""
Configuration settings for VAPS XT 661 GenAI XML Generator
"""

import os
from typing import Dict, List

# Ollama Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_TIMEOUT = int(os.getenv("OLLAMA_TIMEOUT", "60"))

# Supported AI Models
SUPPORTED_MODELS = {
    "codellama": {
        "name": "Code Llama",
        "description": "Meta's Code Llama model optimized for code generation",
        "context_length": 4096,
        "best_for": ["XML generation", "Code structure", "Technical documentation"]
    },
    "llama3.2": {
        "name": "Llama 3.2",
        "description": "Latest Llama model with improved reasoning capabilities",
        "context_length": 8192,
        "best_for": ["General purpose", "Complex reasoning", "Detailed descriptions"]
    },
    "mistral": {
        "name": "Mistral 7B",
        "description": "Fast and efficient model with good performance",
        "context_length": 4096,
        "best_for": ["Quick generation", "Simple widgets", "Batch processing"]
    },
    "deepseek-coder": {
        "name": "DeepSeek Coder",
        "description": "Specialized coding model with excellent XML capabilities",
        "context_length": 4096,
        "best_for": ["XML/HTML generation", "Structured data", "Code quality"]
    }
}

# VAPS XT 661 Widget Types
WIDGET_TYPES = {
    "Button": {
        "description": "Interactive button widget for user input",
        "required_attributes": ["Label", "Position", "Size"],
        "optional_attributes": ["BackgroundColor", "TextColor", "OnClick", "Tooltip"]
    },
    "TextDisplay": {
        "description": "Text display widget for showing information",
        "required_attributes": ["Text", "Position", "Size"],
        "optional_attributes": ["BackgroundColor", "TextColor", "FontSize", "Alignment"]
    },
    "Gauge": {
        "description": "Gauge widget for displaying numeric values",
        "required_attributes": ["Type", "Position", "Size", "Range"],
        "optional_attributes": ["Units", "RedLine", "YellowLine", "NeedleColor", "BackgroundColor"]
    },
    "LED": {
        "description": "LED indicator for status display",
        "required_attributes": ["Position", "Size", "Color"],
        "optional_attributes": ["State", "Blinking", "BlinkRate", "Tooltip"]
    },
    "InputField": {
        "description": "Input field for user data entry",
        "required_attributes": ["Position", "Size"],
        "optional_attributes": ["Placeholder", "DataType", "Validation", "BackgroundColor", "BorderColor"]
    },
    "Slider": {
        "description": "Slider control for value selection",
        "required_attributes": ["Position", "Size", "Range"],
        "optional_attributes": ["Orientation", "Step", "Value", "HandleColor", "TrackColor"]
    },
    "ProgressBar": {
        "description": "Progress bar for showing completion status",
        "required_attributes": ["Position", "Size", "Range"],
        "optional_attributes": ["Value", "Orientation", "FillColor", "BackgroundColor", "ShowText"]
    },
    "Chart": {
        "description": "Chart widget for displaying data trends",
        "required_attributes": ["Type", "Position", "Size"],
        "optional_attributes": ["XAxis", "YAxis", "GridLines", "Legend", "DataSeries"]
    }
}

# Color Palette for Aviation Displays
AVIATION_COLORS = {
    "primary": "#1e3a8a",      # Deep blue
    "secondary": "#10b981",    # Green
    "warning": "#f59e0b",      # Amber
    "danger": "#ef4444",       # Red
    "info": "#3b82f6",         # Blue
    "success": "#22c55e",      # Green
    "white": "#ffffff",
    "black": "#000000",
    "gray": "#6b7280",
    "light_gray": "#f3f4f6",
    "dark_gray": "#374151"
}

# XML Templates
XML_HEADER = '<?xml version="1.0" encoding="UTF-8"?>'

# Application Settings
APP_SETTINGS = {
    "page_title": "VAPS XT 661 GenAI XML Generator",
    "page_icon": "🚁",
    "layout": "wide",
    "sidebar_state": "expanded",
    "max_xml_size": 1024 * 1024,  # 1MB max XML file size
    "generation_timeout": 120,     # 2 minutes timeout for XML generation
    "demo_mode_default": False
}

# Prompt Engineering Templates
PROMPT_TEMPLATES = {
    "basic": """
Generate a VAPS XT 661 XML widget based on this description:
{description}

Requirements:
- Use proper XML syntax
- Include all necessary attributes
- Follow VAPS XT 661 standards
""",
    
    "detailed": """
You are an expert XML generator for VAPS XT 661 aircraft display systems.

Create a complete, valid XML widget definition for:
{description}

XML Requirements:
1. Valid XML syntax with proper nesting
2. Include position (x, y coordinates)
3. Include size (width, height)
4. Specify colors using standard names or hex codes
5. Add appropriate attributes for the widget type
6. Follow VAPS XT 661 naming conventions

Output only the XML code, no explanations.
""",
    
    "aviation_focused": """
As an avionics display system expert, generate VAPS XT 661 XML for:
{description}

Consider:
- Aviation color standards (green=normal, amber=caution, red=warning)
- Pilot ergonomics and readability
- Certification requirements for display systems
- Standard cockpit layout conventions

Generate clean, standards-compliant XML only.
"""
}

# File Extensions
SUPPORTED_EXTENSIONS = [".xml", ".vaps", ".display"]

# Default Examples
DEFAULT_EXAMPLES = [
    {
        "name": "Engine RPM Gauge",
        "description": "Create a circular RPM gauge for engine monitoring, range 0-6000 RPM, positioned at (200, 100), diameter 120px, with red line at 5500 RPM and amber line at 5000 RPM",
        "category": "Gauge"
    },
    {
        "name": "Emergency Stop Button",
        "description": "Create a large red emergency stop button labeled 'EMERGENCY STOP' at position (400, 300), size 180x60, with white text and immediate action trigger",
        "category": "Button"
    },
    {
        "name": "Altitude Display",
        "description": "Create a digital altitude display showing current altitude in feet, positioned at (100, 50), size 150x40, green text on black background, updating in real-time",
        "category": "TextDisplay"
    },
    {
        "name": "Fuel Level Indicator",
        "description": "Create a vertical fuel level bar gauge at position (50, 150), size 30x200, showing percentage from 0-100%, with amber at 25% and red at 10%",
        "category": "ProgressBar"
    },
    {
        "name": "Navigation Input",
        "description": "Create a heading input field for navigation, positioned at (250, 200), size 80x30, accepting values 0-359 degrees, with validation and degree symbol",
        "category": "InputField"
    }
]