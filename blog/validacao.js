function cadastrar(){
    let email = document.getElementById('email').value;
    let senha  = document.getElementById('senha').value;
    let success = document.getElementById('success');
    let error = document.getElementById('error');
    if(email.length !== 0 && senha.length !== 0){
        success.style.display = 'block';
        error.style.display = 'none';
    }else{
        success.style.display = 'none';
        error.style.display = 'block';
    }

    
}