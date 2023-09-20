document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const fname = document.getElementById('fname').value;
    const lname = document.getElementById('lname').value;
    const state = document.getElementById('state').value;
    const pincode = document.getElementById('pincode').value;
    const city  = document.getElementById('city').value;
    const residence = document.getElementById('residence').value;
    const phoneno = document.getElementById('phoneno').value;

    if (!fname || !phoneno || !pincode || !state ) {
        alert('It is mendatery to fill all the details which there mention');
        return;
    }

    // Simulate login (replace this with your actual login logic)
    alert('Logged in as: ' + username);
});
