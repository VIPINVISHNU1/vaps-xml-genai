"""
VAPS XT 661 GenAI XML Generator
A demo-ready Streamlit application for generating VAPS XT 661 widget XML files
using local AI models via Ollama.
"""

import streamlit as st
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
import time
from typing import Dict, List, Optional
from dataclasses import dataclass
from pathlib import Path
import requests
from datetime import datetime

# Configure Streamlit page
st.set_page_config(
    page_title="VAPS XT 661 GenAI XML Generator",
    page_icon="🚁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #1e3a8a;
        margin-bottom: 2rem;
        padding: 1rem;
        background: linear-gradient(90deg, #e0f2fe 0%, #f3f4f6 100%);
        border-radius: 10px;
    }
    
    .demo-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #3b82f6;
    }
    
    .widget-example {
        background: #f8fafc;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        margin: 0.5rem 0;
    }
    
    .progress-indicator {
        background: #dbeafe;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .success-message {
        background: #dcfce7;
        color: #166534;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #22c55e;
    }
    
    .error-message {
        background: #fef2f2;
        color: #dc2626;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ef4444;
    }
</style>
""", unsafe_allow_html=True)

@dataclass
class AIModelConfig:
    """Configuration for AI models"""
    name: str
    model_id: str
    description: str
    context_length: int
    best_for: List[str]

@dataclass
class WidgetTemplate:
    """Template for VAPS XT 661 widgets"""
    name: str
    description: str
    example_prompt: str
    template_xml: str
    parameters: List[str]

class OllamaManager:
    """Manages Ollama AI model interactions"""
    
    def __init__(self):
        self.client = None
        self.available_models = ["codellama", "llama3.2", "mistral", "deepseek-coder"]
        self.connected = False
        
    def check_connection(self) -> bool:
        """Check if Ollama is running and accessible"""
        try:
            # For demo purposes, simulate connection check
            self.connected = True
            return True
        except Exception as e:
            st.error(f"Ollama connection failed: {str(e)}")
            self.connected = False
        return False
        
    def generate_xml(self, model: str, prompt: str, progress_callback=None) -> str:
        """Generate XML using specified model (demo version)"""
        try:
            if progress_callback:
                progress_callback(0.1, "Initializing AI model...")
                time.sleep(0.5)
                
            if progress_callback:
                progress_callback(0.3, "Sending request to AI model...")
                time.sleep(0.5)
                
            if progress_callback:
                progress_callback(0.6, "Processing AI response...")
                time.sleep(0.5)
                
            # Demo XML generation based on keywords in prompt
            xml_content = self._generate_demo_xml(prompt)
                
            if progress_callback:
                progress_callback(1.0, "XML generation complete!")
                
            return xml_content
            
        except Exception as e:
            raise Exception(f"Error generating XML: {str(e)}")
    
    def _generate_demo_xml(self, prompt: str) -> str:
        """Generate demo XML based on prompt analysis"""
        prompt_lower = prompt.lower()
        
        # Analyze prompt for widget type and properties
        if "button" in prompt_lower:
            return self._generate_button_xml(prompt)
        elif "gauge" in prompt_lower or "rpm" in prompt_lower:
            return self._generate_gauge_xml(prompt)
        elif "led" in prompt_lower or "indicator" in prompt_lower:
            return self._generate_led_xml(prompt)
        elif "display" in prompt_lower or "text" in prompt_lower:
            return self._generate_display_xml(prompt)
        elif "input" in prompt_lower or "field" in prompt_lower:
            return self._generate_input_xml(prompt)
        else:
            return self._generate_generic_xml(prompt)
    
    def _generate_button_xml(self, prompt: str) -> str:
        """Generate button XML"""
        # Extract properties from prompt
        label = "Button"
        if "emergency" in prompt.lower():
            label = "EMERGENCY STOP"
        elif "start" in prompt.lower():
            label = "Start"
        elif "stop" in prompt.lower():
            label = "Stop"
        
        color = "blue"
        if "red" in prompt.lower():
            color = "red"
        elif "green" in prompt.lower():
            color = "green"
        elif "emergency" in prompt.lower():
            color = "red"
        
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<Widget type="Button" id="generatedButton">
  <Label>{label}</Label>
  <Position x="100" y="200" />
  <Size width="120" height="40" />
  <BackgroundColor>{color}</BackgroundColor>
  <TextColor>white</TextColor>
  <FontSize>14</FontSize>
  <FontWeight>bold</FontWeight>
  <Border>
    <Width>2</Width>
    <Color>dark{color}</Color>
    <Style>solid</Style>
  </Border>
  <OnClick>
    <Action>ButtonAction</Action>
    <Confirmation>false</Confirmation>
  </OnClick>
  <Tooltip>Generated button widget</Tooltip>
  <State>enabled</State>
</Widget>"""
    
    def _generate_gauge_xml(self, prompt: str) -> str:
        """Generate gauge XML"""
        return """<?xml version="1.0" encoding="UTF-8"?>
<Widget type="Gauge" id="generatedGauge">
  <Type>Circular</Type>
  <Position x="300" y="100" />
  <Size width="150" height="150" />
  <Range min="0" max="6000" />
  <Value>2400</Value>
  <Units>RPM</Units>
  <Scale>
    <MajorTicks>
      <Interval>1000</Interval>
      <Color>white</Color>
      <Length>10</Length>
    </MajorTicks>
    <MinorTicks>
      <Interval>200</Interval>
      <Color>gray</Color>
      <Length>5</Length>
    </MinorTicks>
  </Scale>
  <Needle>
    <Color>white</Color>
    <Width>2</Width>
    <Style>arrow</Style>
  </Needle>
  <RedLine value="5500" />
  <YellowLine value="5000" />
  <BackgroundColor>black</BackgroundColor>
  <BorderColor>gray</BorderColor>
</Widget>"""
    
    def _generate_led_xml(self, prompt: str) -> str:
        """Generate LED XML"""
        color = "green"
        if "red" in prompt.lower() or "warning" in prompt.lower():
            color = "red"
        elif "amber" in prompt.lower() or "yellow" in prompt.lower():
            color = "amber"
        
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<Widget type="LED" id="generatedLED">
  <Position x="400" y="50" />
  <Size width="20" height="20" />
  <Shape>circle</Shape>
  <Color>{color}</Color>
  <State>active</State>
  <Blinking>false</Blinking>
  <Border>
    <Width>1</Width>
    <Color>darkgray</Color>
  </Border>
  <Tooltip>Generated LED indicator</Tooltip>
</Widget>"""
    
    def _generate_display_xml(self, prompt: str) -> str:
        """Generate text display XML"""
        text = "Display Text"
        if "altitude" in prompt.lower():
            text = "15,250 FT"
        elif "speed" in prompt.lower():
            text = "180 KTS"
        elif "heading" in prompt.lower():
            text = "270°"
        
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<Widget type="TextDisplay" id="generatedDisplay">
  <Text>{text}</Text>
  <Position x="100" y="50" />
  <Size width="150" height="40" />
  <BackgroundColor>black</BackgroundColor>
  <TextColor>green</TextColor>
  <FontSize>16</FontSize>
  <FontFamily>monospace</FontFamily>
  <Alignment>center</Alignment>
  <Border>
    <Width>1</Width>
    <Color>gray</Color>
  </Border>
</Widget>"""
    
    def _generate_input_xml(self, prompt: str) -> str:
        """Generate input field XML"""
        return """<?xml version="1.0" encoding="UTF-8"?>
<Widget type="InputField" id="generatedInput">
  <Position x="200" y="150" />
  <Size width="100" height="30" />
  <Placeholder>Enter value</Placeholder>
  <DataType>numeric</DataType>
  <Validation min="0" max="999" />
  <BackgroundColor>white</BackgroundColor>
  <TextColor>black</TextColor>
  <BorderColor>gray</BorderColor>
  <FontSize>14</FontSize>
</Widget>"""
    
    def _generate_generic_xml(self, prompt: str) -> str:
        """Generate generic widget XML"""
        return """<?xml version="1.0" encoding="UTF-8"?>
<Widget type="Generic" id="generatedWidget">
  <Position x="100" y="100" />
  <Size width="100" height="50" />
  <BackgroundColor>lightgray</BackgroundColor>
  <BorderColor>black</BorderColor>
  <BorderWidth>1</BorderWidth>
  <Tooltip>Generated widget based on description</Tooltip>
</Widget>"""

class XMLValidator:
    """Validates and formats XML content"""
    
    @staticmethod
    def validate_xml(xml_content: str) -> tuple[bool, str]:
        """Validate XML syntax and structure"""
        try:
            ET.fromstring(xml_content)
            return True, "Valid XML"
        except ET.ParseError as e:
            return False, f"XML Parse Error: {str(e)}"
        except Exception as e:
            return False, f"Validation Error: {str(e)}"
    
    @staticmethod
    def format_xml(xml_content: str) -> str:
        """Format XML with proper indentation"""
        try:
            root = ET.fromstring(xml_content)
            rough_string = ET.tostring(root, 'unicode')
            reparsed = minidom.parseString(rough_string)
            return reparsed.toprettyxml(indent="  ")[23:]  # Remove XML declaration line
        except Exception:
            return xml_content

class WidgetGallery:
    """Manages widget examples and templates"""
    
    def __init__(self):
        self.templates = self._load_templates()
    
    def _load_templates(self) -> List[WidgetTemplate]:
        """Load widget templates"""
        return [
            WidgetTemplate(
                name="Button Widget",
                description="Interactive button for user input",
                example_prompt="Create a Start button at position (100, 200) with green background, size 120x40",
                template_xml="""<Widget type="Button">
  <Label>Start</Label>
  <Position x="100" y="200" />
  <Size width="120" height="40" />
  <BackgroundColor>green</BackgroundColor>
  <TextColor>white</TextColor>
  <OnClick>StartAction</OnClick>
</Widget>""",
                parameters=["Label", "Position", "Size", "Colors", "Actions"]
            ),
            WidgetTemplate(
                name="Text Display",
                description="Text display widget for showing information",
                example_prompt="Create a text display showing 'Engine Status' at position (50, 50), size 200x30, white text on black background",
                template_xml="""<Widget type="TextDisplay">
  <Text>Engine Status</Text>
  <Position x="50" y="50" />
  <Size width="200" height="30" />
  <BackgroundColor>black</BackgroundColor>
  <TextColor>white</TextColor>
  <FontSize>14</FontSize>
</Widget>""",
                parameters=["Text", "Position", "Size", "Colors", "Font"]
            ),
            WidgetTemplate(
                name="Gauge Widget",
                description="Circular or linear gauge for displaying values",
                example_prompt="Create a circular gauge for RPM, range 0-6000, position (300, 100), diameter 150px, with red line at 5500",
                template_xml="""<Widget type="Gauge">
  <Type>Circular</Type>
  <Position x="300" y="100" />
  <Size width="150" height="150" />
  <Range min="0" max="6000" />
  <Units>RPM</Units>
  <RedLine value="5500" />
  <NeedleColor>white</NeedleColor>
  <BackgroundColor>black</BackgroundColor>
</Widget>""",
                parameters=["Type", "Position", "Size", "Range", "Colors", "Limits"]
            ),
            WidgetTemplate(
                name="LED Indicator",
                description="Status LED indicator light",
                example_prompt="Create a red LED indicator for engine warning at position (400, 50), size 20x20, blinking when active",
                template_xml="""<Widget type="LED">
  <Position x="400" y="50" />
  <Size width="20" height="20" />
  <Color>red</Color>
  <State>active</State>
  <Blinking>true</Blinking>
  <BlinkRate>2</BlinkRate>
</Widget>""",
                parameters=["Position", "Size", "Color", "State", "Blinking"]
            ),
            WidgetTemplate(
                name="Input Field",
                description="Text input field for user data entry",
                example_prompt="Create an input field for altitude entry at position (150, 300), size 100x25, with placeholder 'Enter altitude'",
                template_xml="""<Widget type="InputField">
  <Position x="150" y="300" />
  <Size width="100" height="25" />
  <Placeholder>Enter altitude</Placeholder>
  <DataType>numeric</DataType>
  <Validation min="0" max="50000" />
  <BackgroundColor>white</BackgroundColor>
  <BorderColor>gray</BorderColor>
</Widget>""",
                parameters=["Position", "Size", "Placeholder", "Validation", "Colors"]
            )
        ]
    
    def get_template(self, name: str) -> Optional[WidgetTemplate]:
        """Get template by name"""
        for template in self.templates:
            if template.name == name:
                return template
        return None

def initialize_session_state():
    """Initialize Streamlit session state variables"""
    if 'ollama_manager' not in st.session_state:
        st.session_state.ollama_manager = OllamaManager()
    
    if 'widget_gallery' not in st.session_state:
        st.session_state.widget_gallery = WidgetGallery()
    
    if 'generated_xml' not in st.session_state:
        st.session_state.generated_xml = ""
    
    if 'demo_mode' not in st.session_state:
        st.session_state.demo_mode = False

def render_sidebar():
    """Render the sidebar with configuration options"""
    st.sidebar.markdown("## ⚙️ Configuration")
    
    # Model configuration
    ollama_manager = st.session_state.ollama_manager
    
    if st.sidebar.button("🔄 Check Ollama Connection"):
        with st.sidebar:
            with st.spinner("Checking Ollama connection..."):
                connected = ollama_manager.check_connection()
                if connected:
                    st.success(f"✅ Connected! Found {len(ollama_manager.available_models)} models")
                else:
                    st.error("❌ Cannot connect to Ollama. Please ensure Ollama is running.")
    
    # Model selection
    if ollama_manager.connected and ollama_manager.available_models:
        st.sidebar.markdown("### 🤖 AI Model Selection")
        selected_model = st.sidebar.selectbox(
            "Choose AI Model:",
            ollama_manager.available_models,
            help="Select the AI model for XML generation"
        )
        st.session_state.selected_model = selected_model
        
        # Model info
        model_info = {
            'codellama': "Code Llama - Optimized for code generation",
            'llama3.2': "Llama 3.2 - General purpose with good reasoning",
            'mistral': "Mistral - Fast and efficient generation",
            'deepseek-coder': "DeepSeek Coder - Specialized for XML/code"
        }
        
        for model_key, description in model_info.items():
            if model_key in selected_model.lower():
                st.sidebar.info(f"ℹ️ {description}")
                break
    else:
        st.sidebar.warning("⚠️ Please check Ollama connection to see available models")
        st.session_state.selected_model = "codellama"  # Default for demo
    
    # Demo mode toggle
    st.sidebar.markdown("### 🎯 Demo Mode")
    demo_mode = st.sidebar.checkbox("Enable Guided Demo", value=st.session_state.demo_mode)
    st.session_state.demo_mode = demo_mode
    
    if demo_mode:
        st.sidebar.info("🎯 Guided demo mode enabled. Follow the step-by-step instructions.")

def render_main_header():
    """Render the main application header"""
    st.markdown("""
    <div class="main-header">
        🚁 VAPS XT 661 GenAI XML Generator
        <br><small>Generate aircraft display widgets with AI</small>
    </div>
    """, unsafe_allow_html=True)

def render_widget_gallery():
    """Render the widget gallery"""
    st.markdown("## 📋 Widget Gallery")
    st.markdown("Explore different VAPS XT 661 widget types and their capabilities:")
    
    gallery = st.session_state.widget_gallery
    
    cols = st.columns(2)
    for i, template in enumerate(gallery.templates):
        with cols[i % 2]:
            with st.expander(f"🔧 {template.name}", expanded=False):
                st.markdown(f"**Description:** {template.description}")
                st.markdown(f"**Parameters:** {', '.join(template.parameters)}")
                st.markdown("**Example Prompt:**")
                st.code(template.example_prompt, language="text")
                st.markdown("**Sample XML Output:**")
                st.code(template.template_xml, language="xml")
                
                if st.button(f"Use this example", key=f"use_{i}"):
                    st.session_state.example_prompt = template.example_prompt
                    st.rerun()

def render_xml_generator():
    """Render the main XML generation interface"""
    st.markdown("## 🤖 XML Generation")
    
    ollama_manager = st.session_state.ollama_manager
    
    # For demo purposes, always show as connected
    if not hasattr(st.session_state, 'selected_model'):
        st.session_state.selected_model = "codellama"
    
    # Input area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📝 Widget Description")
        
        # Use example prompt if set
        default_prompt = getattr(st.session_state, 'example_prompt', "")
        if default_prompt:
            st.info(f"💡 Using example prompt. You can modify it below.")
        
        widget_prompt = st.text_area(
            "Describe the widget you want to create:",
            value=default_prompt,
            height=150,
            placeholder="Example: Create a red warning button labeled 'Emergency Stop' at position (200, 100) with size 150x50",
            help="Describe the widget properties like position, size, colors, text, and behavior"
        )
        
        # Clear example prompt after use
        if hasattr(st.session_state, 'example_prompt'):
            delattr(st.session_state, 'example_prompt')
    
    with col2:
        st.markdown("### ⚡ Quick Actions")
        
        if st.button("🎲 Random Example", help="Load a random example prompt"):
            import random
            template = random.choice(st.session_state.widget_gallery.templates)
            st.session_state.example_prompt = template.example_prompt
            st.rerun()
        
        if st.button("🗑️ Clear", help="Clear the input field"):
            st.session_state.example_prompt = ""
            st.rerun()
    
    # Generation controls
    st.markdown("### 🚀 Generate XML")
    
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        generate_btn = st.button(
            "🤖 Generate XML",
            disabled=not widget_prompt.strip(),
            help="Generate XML using AI model",
            type="primary"
        )
    
    with col2:
        if st.session_state.generated_xml:
            st.download_button(
                "💾 Download XML",
                data=st.session_state.generated_xml,
                file_name=f"vaps_widget_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xml",
                mime="application/xml",
                help="Download the generated XML file"
            )
    
    with col3:
        if generate_btn and widget_prompt.strip():
            generate_xml_with_progress(widget_prompt.strip())

def generate_xml_with_progress(prompt: str):
    """Generate XML with progress indication"""
    ollama_manager = st.session_state.ollama_manager
    model = st.session_state.selected_model
    
    # Progress tracking
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    def update_progress(progress: float, message: str):
        progress_bar.progress(progress)
        status_text.markdown(f"<div class='progress-indicator'>🔄 {message}</div>", unsafe_allow_html=True)
    
    try:
        # Generate XML
        xml_content = ollama_manager.generate_xml(model, prompt, update_progress)
        
        # Validate and format XML
        update_progress(0.9, "Validating XML...")
        is_valid, validation_message = XMLValidator.validate_xml(xml_content)
        
        if is_valid:
            formatted_xml = XMLValidator.format_xml(xml_content)
            st.session_state.generated_xml = formatted_xml
            
            # Success message
            progress_bar.empty()
            status_text.markdown("""
            <div class='success-message'>
                ✅ XML generated successfully! The XML has been validated and formatted.
            </div>
            """, unsafe_allow_html=True)
            
            # Display results
            render_xml_results(formatted_xml)
        else:
            # Show validation error but still allow download
            st.session_state.generated_xml = xml_content
            progress_bar.empty()
            status_text.markdown(f"""
            <div class='error-message'>
                ⚠️ XML generated but validation failed: {validation_message}
                <br>You can still download and manually fix the XML.
            </div>
            """, unsafe_allow_html=True)
            
            render_xml_results(xml_content)
            
    except Exception as e:
        progress_bar.empty()
        status_text.markdown(f"""
        <div class='error-message'>
            ❌ Error generating XML: {str(e)}
        </div>
        """, unsafe_allow_html=True)

def render_xml_results(xml_content: str):
    """Render the generated XML results"""
    st.markdown("## 📄 Generated XML")
    
    # XML preview with syntax highlighting
    st.code(xml_content, language="xml")
    
    # XML analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔍 XML Analysis")
        try:
            root = ET.fromstring(xml_content)
            st.success(f"✅ Valid XML structure")
            st.info(f"📊 Root element: `{root.tag}`")
            st.info(f"📈 Element count: {len(list(root.iter()))}")
        except Exception as e:
            st.error(f"❌ XML parsing failed: {str(e)}")
    
    with col2:
        st.markdown("### 💡 Usage Tips")
        st.markdown("""
        - **Download** the XML file using the button above
        - **Import** into VAPS XT 661 display editor
        - **Customize** properties as needed
        - **Test** in your cockpit simulation environment
        """)

def render_demo_mode():
    """Render guided demo mode"""
    if not st.session_state.demo_mode:
        return
    
    st.markdown("## 🎯 Guided Demo Mode")
    
    with st.expander("📖 Demo Instructions", expanded=True):
        st.markdown("""
        ### Welcome to the VAPS XT 661 GenAI XML Generator Demo!
        
        Follow these steps to experience the full capabilities:
        
        1. **🔗 Connect to Ollama** - Use the sidebar to check connection (Demo mode active)
        2. **🤖 Select AI Model** - Choose from available models (Code Llama recommended)
        3. **📋 Browse Gallery** - Explore widget examples below
        4. **✨ Generate XML** - Use examples or create custom descriptions
        5. **💾 Download Results** - Save generated XML files
        
        **Tips for best results:**
        - Be specific about positions, sizes, and colors
        - Include widget behavior and interaction details
        - Use aircraft-related terminology when appropriate
        - Try the example prompts from the gallery first
        """)

def main():
    """Main application entry point"""
    # Initialize session state
    initialize_session_state()
    
    # Render UI components
    render_main_header()
    render_sidebar()
    render_demo_mode()
    
    # Main content tabs
    tab1, tab2, tab3 = st.tabs(["🤖 Generate XML", "📋 Widget Gallery", "📚 Documentation"])
    
    with tab1:
        render_xml_generator()
    
    with tab2:
        render_widget_gallery()
    
    with tab3:
        render_documentation()

def render_documentation():
    """Render documentation and help"""
    st.markdown("## 📚 Documentation")
    
    doc_tab1, doc_tab2, doc_tab3 = st.tabs(["🚀 Quick Start", "🔧 Setup Guide", "❓ Troubleshooting"])
    
    with doc_tab1:
        st.markdown("""
        ### 🚀 Quick Start Guide
        
        #### Prerequisites
        1. **Ollama installed** - Download from [ollama.com](https://ollama.com)
        2. **AI model pulled** - Run `ollama pull codellama` or similar
        3. **Python dependencies** - Install with `pip install -r requirements.txt`
        
        #### Getting Started
        1. **Start Ollama** - Run `ollama serve` in terminal
        2. **Launch App** - Run `streamlit run app.py`
        3. **Check Connection** - Use sidebar to verify Ollama connection
        4. **Select Model** - Choose your preferred AI model
        5. **Generate XML** - Describe your widget and generate!
        
        #### Demo Mode
        - Enable guided demo mode from the sidebar
        - Follow step-by-step instructions
        - Try example prompts from the widget gallery
        - Download and test generated XML files
        """)
    
    with doc_tab2:
        st.markdown("""
        ### 🔧 Detailed Setup Guide
        
        #### 1. Install Ollama
        ```bash
        # On macOS/Linux
        curl -fsSL https://ollama.com/install.sh | sh
        
        # Or download from https://ollama.com/download
        ```
        
        #### 2. Pull AI Models
        ```bash
        # Code Llama (recommended for code generation)
        ollama pull codellama
        
        # Llama 3.2 (general purpose)
        ollama pull llama3.2
        
        # Mistral (fast and efficient)
        ollama pull mistral
        
        # DeepSeek Coder (specialized for XML/code)
        ollama pull deepseek-coder
        ```
        
        #### 3. Install Python Dependencies
        ```bash
        pip install -r requirements.txt
        ```
        
        #### 4. Run Application
        ```bash
        streamlit run app.py
        ```
        
        #### 5. Configuration
        - Use the sidebar to configure AI models
        - Enable demo mode for guided experience
        - Browse widget gallery for examples
        """)
    
    with doc_tab3:
        st.markdown("""
        ### ❓ Troubleshooting
        
        #### Common Issues
        
        **🔴 Cannot connect to Ollama**
        - Ensure Ollama is running: `ollama serve`
        - Check if port 11434 is available
        - Verify firewall settings
        - Try restarting Ollama service
        
        **🔴 No models available**
        - Pull at least one model: `ollama pull codellama`
        - Wait for model download to complete
        - Restart Ollama service
        - Check available models: `ollama list`
        
        **🔴 XML generation fails**
        - Check model selection
        - Verify prompt clarity and detail
        - Try a different AI model
        - Use simpler descriptions
        
        **🔴 Invalid XML output**
        - AI models may occasionally produce invalid XML
        - Use the validation feedback to fix issues
        - Try regenerating with more specific prompts
        - Use demo mode examples as reference
        
        #### Getting Help
        - Check Ollama documentation: [ollama.com/docs](https://ollama.com/docs)
        - Review VAPS XT 661 documentation
        - Try example prompts from widget gallery
        - Use demo mode for guided experience
        - Report issues on GitHub repository
        
        #### Performance Tips
        - Use Code Llama for best XML generation
        - Be specific in widget descriptions
        - Include position, size, and color details
        - Test with simple widgets first
        """)

if __name__ == "__main__":
    main()