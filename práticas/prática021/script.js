function checar(){
    let nome = document.getElementById('nome')
    let resultado = document.getElementById('res')
    if(nome == "Eric"){
        resultado.innerText = "Olá, lindo"
    }else{
        resultado.innerHTML = "Olá, ", nome 
    }
}