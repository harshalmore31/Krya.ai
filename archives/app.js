document.getElementById('terminal-input').addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
        const input = e.target.value;
        const output = document.getElementById('terminal-output');
        output.value += `> ${input}\n`;
        e.target.value = '';

        // Simulate command processing
        setTimeout(() => {
            output.value += `Output: [Processed: ${input}]\n\n`;
            output.scrollTop = output.scrollHeight;
        }, 500);
    }
});
