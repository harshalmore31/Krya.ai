import os
import google.generativeai as genai
from functions.config import configure_model


def generate_code(prompt):
    model = configure_model()
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [prompt],
            },
        ]
    )
    response = chat_session.send_message(prompt)
    generated_code = response.text
    if generated_code.startswith("```python"):
        generated_code = generated_code[len("```python"):].strip()
    if generated_code.endswith("```"):
        generated_code = generated_code[:-len("```")].strip()
    script_path = os.path.join(os.getcwd(), "src/generated_output/generated_output.py")

    with open(script_path, "w") as f:
        f.write(generated_code)

    return generated_code
