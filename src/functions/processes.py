import base64
import pyperclip
import streamlit as st
from functions.gen import generate_code
from functions.exec import run_script
import os
from dotenv import load_dotenv

def process_prompt(prompt):
    generated_code = generate_code(prompt)
    execution_message = run_script()
    return generated_code, execution_message

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def copy_to_clipboard(text, button_key):
    if st.button("📋 Copy", key=button_key):
        pyperclip.copy(text)
        st.success("Copied to clipboard!")

def check_api():
    load_dotenv()
    return bool(os.getenv("GOOGLE_API_KEY"))
