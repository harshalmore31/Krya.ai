import streamlit as st
from pydeck.bindings.map_styles import styles
from functions.processes import process_prompt,copy_to_clipboard, check_api
from dotenv import load_dotenv
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_full_path(relative_path):
    return os.path.join(BASE_DIR, relative_path)

# Usage
logo_path = "https://raw.githubusercontent.com/devdattatalele/Krya.ai/dd43de46ca6e19e7dfcae0a3eff27d889d984531/assests/krya_logo.svg"
styles_path=get_full_path("UI/style.css")
# Streamlit UI Design
st.set_page_config(page_icon=logo_path,page_title="Krya.ai Automation Console", layout="wide",initial_sidebar_state="expanded")

# Custom CSS for modern look and adjustments
with open(styles_path, 'r') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar with improved styling
with st.sidebar:

    st.markdown(
        f"""
        <div style="display: flex; justify-content: 0; align-items: center; height: 15vh; flex-direction: column;">
            <div style="display: flex; align-items: center;">
                <img src="{logo_path}" alt="Logo" style="width: 60px; margin-right: 20px;">
                <h1 style="color: #007acc; font-family:comic sans ms ; font-size: 3rem; margin: 0;">
                      Krya.AI
                </h1></div></div>
        """,
        unsafe_allow_html=True,
    )
    google_api_key = st.text_input(
        "Enter your Gemini API key:",
        value=st.session_state.get('GOOGLE_API_KEY', ''),
        type="password",
        help="You can find your Gemini API key on the [Gemini API](https://aistudio.google.com/apikey).",
    )
    if google_api_key:
        st.session_state['openai_api_key'] = google_api_key
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
            </a><a href="https://linkedin.com/in/devdatta-talele" target="_blank" class="social-link">
                <i class="fab fa-linkedin"></i> LinkedIn
        </a></div>
    """, unsafe_allow_html=True)

# Main Content Centered
st.markdown("""
    <div class="main-container">
    <h1 style="font-size: 3rem; margin: 0;"> Krya.AI </h1>
    """, unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; font-weight:bold; font-family:comic sans ms; padding-top: 0rem;'> \
            Automated interactions and code execution on local machine </h3>", unsafe_allow_html=True)
user_input = st.text_input("Enter your prompt-", placeholder="e.g., Generate a portfolio website on VS CODE")
execute_button = st.button("Execute")
if execute_button:
    load_dotenv()
    if check_api()==True:
        if execute_button and user_input:
            with st.spinner("Processing your request..."):
                code, execution_status = process_prompt(user_input)
                st.markdown("""<style> .stTextArea {margin-top: -25px;}</style>""",unsafe_allow_html=True,)
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Generated Code")
                    st.code(code, language="python")
                    copy_to_clipboard(code, "copy_code")
                with col2:
                    st.subheader("Execution Status")
                    st.text_area("", execution_status, height=300, key="execution_status")
                    copy_to_clipboard(execution_status, "copy_status")
    else:
        st.error("API not found, Enter the API in sidebar")
        st.stop()

st.markdown("</div>", unsafe_allow_html=True)