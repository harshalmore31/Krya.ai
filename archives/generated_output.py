import pyautogui
import time
import subprocess

try:
    # Open notepad
    pyautogui.hotkey('win')
    time.sleep(2)
    pyautogui.write('notepad')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'n')  # new window
    time.sleep(2)




except Exception as e:
    print(f"An error occurred: {e}")