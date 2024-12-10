import os
import google.generativeai as genai
from dotenv import load_dotenv

with open(r"src\system\instruction.txt", "r", encoding="utf-8") as f:
    instruct = f.read()

# change the path if there is any cross platform issue, as you use Linux

def configure_model():
    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    generation_config = {
        "temperature": 1.55,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction=instruct,

    )
    return model