document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const phoneno  = document.getElementById('phoneno').value;
    const password = document.getElementById('password').value;

    if (!username || !password || !phoneno) {
        alert('It is mendatery to fill all the details which there mention');
        return;
    }

    // Simulate login (replace this with your actual login logic)
    alert('Logged in as: ' + username);
});
