axios = require('axios');
let rondon = axios.get('https://viacep.com.br/ws/87800000/json/')
    .then(response => {
        alert((new Adress(response.data)))
    });
;

function Adress ({cep, ddd}){
    this.cep = cep,
    this.ddd = ddd
}


