# VAPS XT 661 GenAI XML Generator

Generate VAPS XT 661 widget XML files using open-source AI models locally and securely. This is a **demo-ready** application showcasing the power of local AI for XML generation in aviation display systems.

![VAPS XML Generator](https://img.shields.io/badge/VAPS-XT%20661-blue) ![AI Powered](https://img.shields.io/badge/AI-Powered-green) ![Local Processing](https://img.shields.io/badge/Processing-Local-orange) ![Open Source](https://img.shields.io/badge/License-Open%20Source-brightgreen)

## 🚀 Features

### **AI Model Enhancements**
- **Enhanced Code Llama integration** via Ollama for superior XML generation
- **Support for multiple free models**: Code Llama, Llama 3.2, Mistral, DeepSeek Coder
- **Improved prompt engineering** with aviation-specific templates
- **Model selection options** in the UI with performance recommendations

### **Demo-Ready Features**
- **Professional Streamlit web interface** with modern UI and aviation theming
- **Interactive XML preview and validation** with syntax highlighting
- **Gallery of example widgets** with sample outputs and copy-to-use functionality
- **Step-by-step guided demo mode** for easy onboarding
- **Real-time generation progress indicators** with detailed status updates

### **Technical Improvements**
- **Complete Streamlit application** with comprehensive error handling
- **Enhanced XML templates** for various VAPS XT 661 widgets (Button, Gauge, LED, Input, Display)
- **Input validation and sanitization** ensuring XML compliance
- **Download functionality** for generated XML files with timestamp naming
- **Configuration management** for different models and settings

### **Core Capabilities**
- **Local only**: No external API or cloud use - all processing remains on your machine
- **Open Source**: Uses free AI models (Code Llama, Llama 3.2, Mistral)
- **Web UI**: Professional interface for describing and generating widgets
- **XML Validation**: Automatic validation and formatting of generated XML
- **Widget Gallery**: Pre-built examples for common cockpit widgets
- **Aviation Focus**: Color standards (green=normal, amber=caution, red=warning)

## 📋 Requirements

- **[Python 3.9+](https://www.python.org/downloads/)** - Core runtime
- **[Ollama](https://ollama.com/)** - For running AI models locally
- **[Streamlit](https://streamlit.io/)** - Web interface framework

## 🔧 Quick Setup

### 1. Install Ollama and AI Models
```bash
# Install Ollama (see https://ollama.com/download)
curl -fsSL https://ollama.com/install.sh | sh

# Pull recommended models
ollama pull codellama      # Best for XML/code generation
ollama pull llama3.2       # General purpose with good reasoning
ollama pull mistral        # Fast and efficient
ollama pull deepseek-coder # Specialized for XML/code
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
# Start Ollama service (if not running)
ollama serve

# Launch the demo-ready application
streamlit run app.py
```

### 4. Access the Interface
Open your browser to `http://localhost:8501` and enjoy the demo!

## 🎯 Demo Instructions

### **Getting Started**
1. **🔗 Connect to Ollama** - Use the sidebar to check connection status
2. **🤖 Select AI Model** - Choose from available models (Code Llama recommended)
3. **📋 Browse Gallery** - Explore widget examples with copy-to-use functionality
4. **✨ Generate XML** - Use examples or create custom widget descriptions
5. **💾 Download Results** - Save generated XML files for import into VAPS XT 661

### **Demo Mode**
Enable **Guided Demo Mode** from the sidebar for:
- Step-by-step instructions
- Example prompts and expected outputs
- Tips for best results
- Interactive tutorial experience

## 📊 Widget Gallery

The application includes comprehensive examples for:

### **Button Widgets**
- Emergency stop buttons with safety colors
- Start/stop controls with proper styling
- Navigation buttons with aviation standards

### **Gauge Widgets**
- Circular RPM gauges with color bands
- Linear fuel quantity displays
- Multi-range instruments with warning limits

### **Display Widgets**
- Digital altitude readouts with formatting
- Speed indicators with unit display
- Status text with color coding

### **LED Indicators**
- Warning lights with blinking patterns
- Status indicators with multiple states
- Color-coded alert systems

### **Input Fields**
- Heading input with validation (0-359°)
- Altitude entry with range checking
- Numeric controls with unit display

## 💡 Usage Examples

### **Simple Button**
```
Create a Start button at position (100, 200) with green background, size 120x40
```

### **Aviation Gauge**
```
Create a circular RPM gauge for engine monitoring, range 0-6000, position (300, 100), diameter 150px, with red line at 5500 RPM and amber line at 5000 RPM
```

### **Emergency Control**
```
Create a large red emergency stop button labeled 'EMERGENCY STOP' at position (400, 300), size 180x60, with white text and immediate action trigger
```

## 🔍 Technical Details

### **AI Model Integration**
- **Ollama Client**: Local API integration for model communication
- **Progress Tracking**: Real-time feedback during generation
- **Error Handling**: Comprehensive error management and recovery
- **Model Selection**: Dynamic model detection and configuration

### **XML Processing**
- **Validation**: XML syntax and structure verification
- **Formatting**: Automatic indentation and prettification
- **Templates**: Aviation-specific widget templates
- **Standards Compliance**: VAPS XT 661 format compatibility

### **User Interface**
- **Professional Styling**: Aviation-themed CSS and layout
- **Responsive Design**: Works on desktop and tablet devices
- **Progress Indicators**: Visual feedback during operations
- **Error Messages**: Clear, actionable error reporting

## 🛠️ Configuration

### **Model Settings**
- Modify `config.py` for model preferences
- Adjust generation timeouts and parameters
- Configure color schemes and templates

### **UI Customization**
- Update CSS in `app.py` for styling changes
- Modify widget templates in the gallery
- Add new example prompts and outputs

### **Aviation Standards**
- Color coding follows DO-178C guidelines
- Widget positioning uses cockpit ergonomics
- Text sizing optimized for flight conditions

## 🔧 Troubleshooting

### **Connection Issues**
- Ensure Ollama is running: `ollama serve`
- Check port 11434 availability
- Verify firewall settings allow local connections

### **Model Problems**
- Pull at least one model: `ollama pull codellama`
- Wait for complete model download
- Check available models: `ollama list`

### **Generation Failures**
- Use specific widget descriptions
- Include position, size, and color details
- Try different AI models for comparison
- Use gallery examples as reference

### **XML Validation**
- Check generated XML for syntax errors
- Use validation feedback for corrections
- Try regenerating with clearer prompts

## 📖 Documentation

The application includes comprehensive documentation:

- **Quick Start Guide**: Get up and running in minutes
- **Setup Instructions**: Detailed installation and configuration
- **Troubleshooting**: Common issues and solutions
- **Best Practices**: Tips for optimal XML generation

## 🎉 Demo Ready

This application is **production-ready for demonstrations** and includes:

✅ **Professional UI** with aviation theming  
✅ **Interactive examples** with real-time generation  
✅ **Comprehensive documentation** and guided tutorials  
✅ **Error handling** and graceful failure recovery  
✅ **Local processing** ensuring data privacy  
✅ **Multiple AI models** for different use cases  
✅ **XML validation** and formatting  
✅ **Download functionality** for generated files  

## 🔒 Privacy & Security

- **No external APIs**: All processing happens locally
- **No data transmission**: Your widget descriptions stay on your machine
- **Open source models**: Full transparency in AI model selection
- **Local storage**: Generated XML files remain under your control

## 🤝 Contributing

This project welcomes contributions! Areas for enhancement:

- Additional widget templates
- New AI model integrations
- UI/UX improvements
- Documentation updates
- Bug fixes and performance optimizations

## 📄 License

This project uses open-source components:
- **Streamlit**: Apache 2.0 License
- **AI Models**: Various open-source licenses (see model documentation)
- **Application Code**: Open source friendly

---

> **All computation and LLM processing runs locally. No data ever leaves your machine.**

**Ready for demonstration - Professional, capable, and completely local! 🚁✨**