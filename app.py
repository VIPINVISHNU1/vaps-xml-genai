import streamlit as st
import subprocess

PROMPT_TEMPLATE_PATH = "prompt_templates/widget_prompt.txt"

def load_prompt_template():
    try:
        with open(PROMPT_TEMPLATE_PATH, "r") as f:
            return f.read()
    except Exception:
        # Fallback if template file is missing
        return (
            "Given the following widget description, generate a VAPS XT 661-compatible XML file "
            "with all appropriate tags and values.\n\n"
            "Widget Description:\n{widget_desc}\n\nXML Output:"
        )

def generate_xml_with_ollama(user_prompt):
    # Use Ollama CLI to query local Code Llama
    full_prompt = user_prompt
    model = "codellama:latest"
    try:
        result = subprocess.run(
            ["ollama", "run", model, "--prompt", full_prompt],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode != 0:
            return f"Error: {result.stderr}"
        return result.stdout.strip()
    except Exception as e:
        return f"Error running Ollama: {e}"

st.title("VAPS XT 661 XML Generator (Code Llama, Local Only)")

st.markdown("""
Enter your widget properties or a prompt describing the widget(s) you want to generate XML for.
The generation runs locally on your machine using Code Llama (via Ollama).
""")

default_prompt = """\
Create an XML file for a VAPS XT 661 Button widget with:
- Label: 'Start'
- X: 40, Y: 80
- Width: 120, Height: 40
- Color: Blue
"""

prompt_template = load_prompt_template()
user_input = st.text_area("Widget Prompt", value=default_prompt, height=200)

if st.button("Generate XML"):
    st.info("Generating XML with Code Llama locally...")
    # Insert user input into template if needed
    if "{widget_desc}" in prompt_template:
        prompt = prompt_template.replace("{widget_desc}", user_input)
    else:
        prompt = user_input
    xml_output = generate_xml_with_ollama(prompt)
    st.code(xml_output, language="xml")
    st.download_button("Download XML", xml_output, file_name="widget.xml", mime="application/xml")