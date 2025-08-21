# VAPS XT 661 GenAI XML Generator

Generate VAPS XT 661 widget XML files using open-source Code Llama LLM, locally and securely.

## Features

- **Local only**: No external API or cloud use.
- **Open Source**: Uses Code Llama (Meta), commercial-friendly.
- **Web UI**: Enter prompts and generate/download XML.
- **Customizable**: Tweak prompts and examples as needed.

## Requirements

- [Python 3.9+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/) (for running Code Llama locally)
- [Streamlit](https://streamlit.io/) (for web UI)

## Setup

1. **Install Ollama and pull Code Llama:**
    ```sh
    # Install Ollama (see https://ollama.com/download)
    ollama pull codellama:latest
    ```

2. **Install Python dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the app:**
    ```sh
    streamlit run app.py
    ```

## Usage

- Enter your widget properties or requirements as a prompt.
- Click "Generate XML".
- Download the generated XML and upload to VAPS XT 661.

## Example

See `examples/` for sample prompts and XML.

---

> **All computation and LLM runs are local. No data ever leaves your machine.**