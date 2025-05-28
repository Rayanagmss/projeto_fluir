// Funções para autenticação
async function fazerLogin(username, password) {
    const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    const data = await response.json();
    if (data.success) {
        updateAuthUI(true);
    }
    return data;
}

async function fazerLogout() {
    const response = await fetch('http://localhost:5000/logout', {
        method: 'POST'
    });
    const data = await response.json();
    if (data.success) {
        updateAuthUI(false);
    }
}

// Atualiza a UI conforme o estado de login
function updateAuthUI(isLoggedIn) {
    const authButton = document.getElementById('auth-button');
    authButton.innerHTML = isLoggedIn 
        ? `<button onclick="fazerLogout()">Logout</button>`
        : `<button onclick="abrirModalLogin()">Login</button>`;
}

// Verifica estado ao carregar a página
async function checkAuthState() {
    const response = await fetch('http://localhost:5000/check_auth');
    const data = await response.json();
    updateAuthUI(data.logged_in);
}

// Inicialização
document.addEventListener('DOMContentLoaded', checkAuthState);


document.addEventListener('DOMContentLoaded', () => {
    const btn = document.querySelector('.hamburguer-btn');
    const menu = document.getElementById('menu');

    btn.addEventListener('click', () => {
        // Alterna a classe "ativo" no botão e no menu
        btn.classList.toggle('ativo');
        menu.classList.toggle('ativo');
    });
});