const logout = document.getElementById('log_out');

logout.addEventListener('click', async function (e){
    let response = await fetch('http://localhost:8000/en/logout/' ,{
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
     });
        localStorage.removeItem('Token');
        window.location.replace("http://localhost:8000")

});