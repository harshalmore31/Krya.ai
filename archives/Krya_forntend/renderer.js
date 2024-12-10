const terminalOutput = document.getElementById('terminal-output');
const terminalInput = document.getElementById('terminal-input');
const statusElement = document.getElementById('status');
const commandList = document.getElementById('commands');

let commandHistory = [];
let historyIndex = -1;

function appendOutput(text, type = 'command') {
    const output = document.createElement('div');
    output.className = `output-line ${type}`;
    output.textContent = text;
    terminalOutput.appendChild(output);
    terminalOutput.scrollTop = terminalOutput.scrollHeight;
}

async function executeCommand(command) {
    try {
        statusElement.textContent = 'Executing...';
        const result = await window.electronAPI.runPython(command);
        appendOutput(`Output: ${result}`, 'success');
    } catch (error) {
        appendOutput(`Error: ${error}`, 'error');
    } finally {
        statusElement.textContent = 'Ready';
    }
}

terminalInput.addEventListener('keydown', async (e) => {
    if (e.key === 'Enter') {
        const command = terminalInput.value.trim();
        if (command) {
            appendOutput(`> ${command}`);
            commandHistory.push(command);
            historyIndex = commandHistory.length;
            terminalInput.value = '';
            await executeCommand(command);
        }
    } else if (e.key === 'ArrowUp') {
        if (historyIndex > 0) {
            historyIndex--;
            terminalInput.value = commandHistory[historyIndex];
        }
        e.preventDefault();
    } else if (e.key === 'ArrowDown') {
        if (historyIndex < commandHistory.length - 1) {
            historyIndex++;
            terminalInput.value = commandHistory[historyIndex];
        } else {
            historyIndex = commandHistory.length;
            terminalInput.value = '';
        }
        e.preventDefault();
    }
});

commandList.addEventListener('click', (e) => {
    if (e.target.tagName === 'LI') {
        const command = e.target.dataset.command;
        terminalInput.value = command;
        terminalInput.focus();
    }
});
