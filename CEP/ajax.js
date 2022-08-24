function requerirCEP(){
    const cep = document.querySelector("#cep").value;
    let log = document.querySelector("#log");
    if(cep.length != 8){
        log.innerText = "CEP invalido! Necessita-se de 8 digitos!"
    }else{
        log.innerText = "";
        const require = new XMLHttpRequest();
        require.open("GET", `https://viacep.com.br/ws/${cep}/json/`);
        require.send();
        require.onload = function(){
            let obj = JSON.parse(this.responseText);
            alert(`Cidade: ${obj.localidade} Estado: ${obj.uf} DDD: ${obj.ddd}`);
        }
    };
};