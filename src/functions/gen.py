import os
import google.generativeai as genai
from functions.config import configure_model

model = configure_model()

def generate_code(prompt):
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [prompt],
            },
        ]
    )

    # Send the prompt and get the response
    response = chat_session.send_message(prompt)
    generated_code = response.text

    # Clean the generated code
    if generated_code.startswith("```python"):
        generated_code = generated_code[len("```python"):].strip()
    if generated_code.endswith("```"):
        generated_code = generated_code[:-len("```")].strip()

    # Save the code to a file in the specified path
    script_path = os.path.join(os.getcwd(), "src", "backend", "generated_output.py")
    with open(script_path, "w") as f:
        f.write(generated_code)

    return generated_code