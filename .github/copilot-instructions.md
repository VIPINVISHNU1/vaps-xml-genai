# VAPS XT 661 GenAI XML Generator

VAPS XT 661 GenAI XML Generator is a Python Streamlit web application that generates VAPS XT 661 widget XML files using Code Llama LLM running locally via Ollama. The application prioritizes local execution with no external API calls or cloud dependencies.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Bootstrap and Setup
- Check Python version: `python3 --version` (requires Python 3.9+, environment has 3.12+)
- Install Python dependencies: `pip install -r requirements.txt` -- takes 30 seconds. NEVER CANCEL.
- **CRITICAL**: Ollama installation fails in sandbox environments due to network restrictions:
  ```sh
  # This WILL FAIL in sandbox/CI environments
  curl -fsSL https://ollama.com/install.sh | sh
  ```
  Document this limitation when working in restricted environments.

### Build and Run
- **Basic Python app**: `python3 app.py` -- runs immediately, prints welcome message
- **Streamlit web UI**: `streamlit run app.py` -- takes 5 seconds to start. Server runs on localhost:8501
  - NEVER CANCEL the Streamlit server once started
  - Use Ctrl+C to stop when done testing
- **Syntax validation**: `python3 -m py_compile app.py` -- validates Python syntax immediately

### Dependencies and Environment
- **Core dependencies**: streamlit, requests (see requirements.txt)
- **External dependency**: Ollama with Code Llama model (not available in sandbox environments)
- **No build step required**: Direct Python execution
- **No tests exist**: Repository has no test suite or test framework
- **No linting setup**: No flake8, black, or other linting tools configured

## Validation Scenarios

### ALWAYS Test After Changes
1. **Basic functionality**: Run `python3 app.py` and verify welcome message appears
2. **Streamlit server**: 
   - Run `streamlit run app.py`
   - Verify server starts and shows "Local URL: http://localhost:8501"
   - Access the web interface if possible
   - Stop server with Ctrl+C
3. **Syntax validation**: Run `python3 -m py_compile app.py` to catch syntax errors
4. **Dependency check**: Run `pip install -r requirements.txt` to ensure dependencies resolve

### Manual Testing Requirements
- **UI Testing**: When making changes to the Streamlit interface, manually navigate through the web UI
- **XML Generation**: Test the core functionality by entering sample prompts and verifying XML output
- **File Operations**: Verify download functionality works for generated XML files

## Repository Structure

### Key Files and Directories
```
/home/runner/work/vaps-xml-genai/vaps-xml-genai/
├── README.md                    # Main documentation
├── app.py                       # Main application entry point
├── requirements.txt             # Python dependencies (streamlit, requests)
├── examples/
│   ├── sample_prompt.txt       # Example user prompt
│   └── sample_widget.xml       # Example generated XML
└── prompt_templates/
    └── widget_prompt.txt       # LLM prompt template
```

### Common Operations
- **View repository structure**: `ls -la` in repo root
- **Check file contents**: Use `cat` for small files like requirements.txt
- **Edit files**: Focus on app.py for main functionality, examples/ for samples

## Development Guidelines

### Code Changes
- **Main application logic**: Edit `app.py` (currently contains minimal stub code)
- **Dependencies**: Add to `requirements.txt` if needed, then run `pip install -r requirements.txt`
- **Examples**: Add new samples to `examples/` directory
- **Prompts**: Modify `prompt_templates/widget_prompt.txt` for LLM prompt tuning

### Before Committing
- Run `python3 -m py_compile app.py` to check syntax
- Test basic app with `python3 app.py`
- Test Streamlit interface with `streamlit run app.py`
- Verify any new dependencies install correctly

### Known Limitations
- **Ollama unavailable**: Cannot test full LLM functionality in sandbox environments
- **No automated tests**: All validation must be manual
- **No CI/CD**: No GitHub Actions or automated build pipeline
- **Network restrictions**: External downloads and installations may fail

## Time Expectations

- **Dependency installation**: 30 seconds (pip install)
- **App startup**: Immediate (python3 app.py)
- **Streamlit startup**: 5 seconds (streamlit run app.py)
- **Syntax checking**: Immediate (py_compile)

## Troubleshooting

### Common Issues
1. **Import errors**: Run `pip install -r requirements.txt` to ensure dependencies are installed
2. **Streamlit not found**: Verify streamlit was installed correctly in requirements
3. **Port conflicts**: Streamlit defaults to port 8501, may conflict in some environments
4. **Ollama errors**: Expected in sandbox environments due to network restrictions

### Environment Setup
- **Python path issues**: Use `python3` explicitly rather than `python`
- **Permission issues**: Use `pip install --user` if system-wide installation fails
- **Cache issues**: Clear `__pycache__/` directories if seeing import problems

## Quick Reference Commands

```sh
# Setup (run once)
pip install -r requirements.txt

# Development workflow
python3 -m py_compile app.py          # Check syntax
python3 app.py                        # Test basic functionality
streamlit run app.py                  # Test web interface
# Ctrl+C to stop Streamlit

# File operations
ls -la                                # View repository structure
cat requirements.txt                  # Check dependencies
cat examples/sample_prompt.txt        # View example prompts
```

Remember: This application is designed for local-only operation with no external dependencies beyond Ollama/Code Llama. Always validate that changes maintain this privacy-focused design.