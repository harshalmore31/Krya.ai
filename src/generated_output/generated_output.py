import pyautogui
import time
import pyperclip

try:
    pyautogui.hotkey('win')
    time.sleep(2)
    pyautogui.write('VS Code')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(2)



    html_lines = [
        '<!DOCTYPE html>',
        '<html lang="en">',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '    <title>My Portfolio</title>',
        '    <style>',
        '        body {',
        '            font-family: sans-serif;',
        '            margin: 0;',
        '            padding: 0;',
        '            background-color: #f0f0f0;',
        '            color: #333;',
        '        }',
        '        header {',
        '            background-color: #333;',
        '            color: #fff;',
        '            padding: 20px;',
        '            text-align: center;',
        '        }',
        '        nav {',
        '            background-color: #eee;',
        '            padding: 10px;',
        '        }',
        '        nav ul {',
        '            list-style: none;',
        '            margin: 0;',
        '            padding: 0;',
        '            text-align: center;',
        '        }',
        '        nav li {',
        '            display: inline;',
        '            margin: 0 10px;',
        '        }',
        '        nav a {',
        '            text-decoration: none;',
        '            color: #333;',
        '        }',
        '        section {',
        '            padding: 20px;',
        '        }',
        '        footer {',
        '            background-color: #333;',
        '            color: #fff;',
        '            padding: 10px;',
        '            text-align: center;',
        '            position: fixed;',
        '            bottom: 0;',
        '            width: 100%;',

        '        }',
        '    </style>',
        '</head>',
        '<body>',
        '    <header>',
        '        <h1>My Portfolio</h1>',

        '    </header>',
        '    <nav>',
        '        <ul>',
        '            <li><a href="#about">About</a></li>',
        '            <li><a href="#projects">Projects</a></li>',
        '            <li><a href="#contact">Contact</a></li>',
        '        </ul>',
        '    </nav>',
        '    <section id="about">',
        '        <h2>About Me</h2>',
        '        <p>Write something about yourself here.</p>',
        '    </section>',
        '    <section id="projects">',
        '        <h2>My Projects</h2>',
        '        <p>List your projects here.</p>',
        '    </section>',
        '    <section id="contact">',
        '        <h2>Contact Me</h2>',
        '        <p>Your contact information here.</p>',
        '    </section>',
        '    <footer>',

        '        <p>&copy; 2023 My Portfolio</p>',

        '    </footer>',
        '</body>',
        '</html>'
    ]


    for line in html_lines:
        pyperclip.copy(line)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl','backspace')
        pyautogui.press('enter')
        time.sleep(0.01)

    pyautogui.hotkey('ctrl','s')
    time.sleep(1)
    pyautogui.write('index.html')
    time.sleep(1)
    pyautogui.press('enter')

except Exception as e:
    print(f"An error occurred: {e}")