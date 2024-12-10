import streamlit as st
from functions.processes import process_prompt,copy_to_clipboard
from dotenv import load_dotenv
import os

# Streamlit UI Design
st.set_page_config(page_icon="assests\krya_logo.png",page_title="Krya.ai Automation Console", layout="wide",initial_sidebar_state="expanded")

# Custom CSS for modern look and adjustments
with open(r"src\UI\style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar with improved styling
with st.sidebar:
    # Logo and Project Name
    st.image("assests\krya_logo.svg", width=50)
    st.markdown("<h1>Krya AI</h1>", unsafe_allow_html=True)

    google_api_key = st.text_input("Enter your Google API Key", placeholder="e.g., Ax********", type="password")
    save_button = st.button("Save")
    load_dotenv()
    google_api_key_env = os.getenv("GOOGLE_API_KEY")
    if google_api_key_env:
        st.info("API key already loaded.")
    else:
        st.warning("Please enter the API key.")
    if save_button and google_api_key:
        with open(".env", "w") as f:
            f.write(f"GOOGLE_API_KEY={google_api_key}")
        st.success("Google API Key saved")

    st.markdown("### Sample Prompts-")
    st.markdown("<div class='sample-prompts'>", unsafe_allow_html=True)
    st.code("Generate a portfolio website on VS CODE", language="text")
    st.code("Compare Phones Under 20k on different E-commerce websites", language="text")
    st.code("Type Gmail letter to HR about Leave", language="text")
    st.code("Create a simple website and host it on AWS", language="text")
    st.markdown("</div>", unsafe_allow_html=True)

    # Social Links
    st.markdown("---")
    st.markdown("       Developed by Devdatta Talele")

    st.markdown("""
        <div class="social-links">
            <a href="https://github.com/devdattatalele/krya.ai" target="_blank" class="social-link">
                <i class="fab fa-github"></i> GitHub
            </a>
            <a href="https://linkedin.com/in/devdatta-talele" target="_blank" class="social-link">
                <i class="fab fa-linkedin"></i> LinkedIn
            </a>
        </div>
    """, unsafe_allow_html=True)

# Main Content Centered
st.markdown("""
    <div class="main-container">
        <h1>KRYA.AI</h1>
""", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-weight:bold; font-family:comic sans ms; padding-top: 0rem;'> \
            Automated interactions and code execution on local machine </h3>", unsafe_allow_html=True)
user_input = st.text_input("Enter your command", placeholder="e.g., Open Notepad")
execute_button = st.button("Execute")
if execute_button:
    load_dotenv()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        st.error("No API_KEY found. Please enter the API key in the sidebar and save.")
        st.stop()

st.markdown("</div>", unsafe_allow_html=True)

if execute_button and user_input:
    with st.spinner("Processing your request..."):
        code, execution_status = process_prompt(user_input)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Generated Code")
            st.code(code, language="python")
            copy_to_clipboard(code, "copy_code")
        with col2:
            st.subheader("Execution Status")
            st.text_area("", execution_status, height=400, key="execution_status")
            copy_to_clipboard(execution_status, "copy_status")