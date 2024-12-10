// main.js
const { app, BrowserWindow, ipcMain } = require('electron');
const { spawn } = require('child_process');
const path = require('path');

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1200,
        height: 800,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            contextIsolation: true,
            nodeIntegration: false
        },
        backgroundColor: '#1e1e1e'
    });
    mainWindow.loadFile('index.html');
}

app.whenReady().then(createWindow);

ipcMain.handle('execute-command', async (event, command) => {
    console.log(`Executing command: ${command}`);
    
    let process;
    switch (command.toLowerCase()) {
        case 'notepad':
            process = spawn('notepad.exe');
            return 'Launched Notepad';
            
        case 'vscode':
            process = spawn('code');
            return 'Launched VS Code';
            
        case 'pycharm':
            // Adjust the path according to your PyCharm installation
            process = spawn('C:\\Program Files\\JetBrains\\PyCharm\\bin\\pycharm64.exe');
            return 'Launched PyCharm';
            
        case 'camera':
            // You'll need to implement camera functionality
            return 'Camera functionality not implemented';
            
        default:
            throw new Error(`Unknown command: ${command}`);
    }
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});