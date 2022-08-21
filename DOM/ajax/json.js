//solicitando um json com ajax


function puxarCep() {

    let cep = document.querySelector("#cep").value;

    let main = document.querySelector("#caixa");



    if (cep.length != 8) {
        alert('Preencha o CEP com 8 digitos.')
    } else {
        const ajax = new XMLHttpRequest();

        ajax.open("GET", `https://viacep.com.br/ws/${cep}/json/`);

        ajax.send();

        ajax.onload = function () {
            let obj = JSON.parse(this.responseText);
            alert(`Cidade: ${obj.localidade}, Estado: ${obj.uf}, DDD: ${obj.ddd}`)
        }

    }
};