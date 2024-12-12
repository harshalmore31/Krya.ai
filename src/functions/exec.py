import os
import time
import pyautogui

def run_script():
    try:
        pyautogui.hotkey('win')
        time.sleep(1)
        pyautogui.typewrite('cmd\n', interval=0.1)
        pyautogui.hotkey('enter')        # Open command prompt (Windows-specific)
        time.sleep(2)
        pyautogui.hotkey('ctrl','shift','t')
        time.sleep(2)
        # Run the script
        script_path = os.path.join(os.getcwd(), "src", "generated_output", "generated_output.py")
        pyautogui.typewrite(f'python "{script_path}"\n', interval=0.01)

        return "Script execution initiated. Check the terminal for results."

    except Exception as e:
        return f"An error occurred: {e}"
