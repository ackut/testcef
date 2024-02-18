let login = document.getElementById('login');
let password = document.getElementById('password');
let submit = document.getElementById('submit');

submit.addEventListener('click', (event) => {
    cef.emit('login:submit', login.value, password.value);
});