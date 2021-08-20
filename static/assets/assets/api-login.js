const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', async function (e){
    e.preventDefault();
    let formData = {
        username: loginForm.username.value,
        password: loginForm.password.value,
    }

    let response = await fetch('http://localhost:8000/en/api/auth/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
     });

    let responseData = await response.json()

    
    if (response.ok){
    //     // console.log(responseData.token);
    localStorage.setItem('Token', responseData.token)
    window.location.replace("http://localhost:8000")
    }
});