document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const errorP = document.getElementById('error');
    errorP.textContent = '';
    const formData = new FormData(e.target);
    try {
        const response = await fetch('/login', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        errorP.textContent = data.error;
    } catch (err) {
        errorP.textContent = 'Erro ao conectar com o servidor!';
    }
});

