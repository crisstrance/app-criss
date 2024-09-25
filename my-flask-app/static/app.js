document.getElementById('apiButton').addEventListener('click', () => {
    fetch('/api')
        .then(response => response.json())
        .then(data => {
            document.getElementById('apiResponse').innerText = data.message;
        });
});