function promise() {
    let nome = document.querySelector('#nome').value;
    let email = document.querySelector('#email').value;
    let senha = document.querySelector('#senha').value;
    let dados = {
        nome: nome,
        email: email,
        senha: senha
    };
    if (nome.length != 0 && email.length != 0 && senha.length != 0) {
        axios.post('https://webhook.site/1fbb4d21-f15f-4170-9b35-716ae7af715a', dados)
            .then(function (response) {
                if (response.data === 'success') {
                    alert('Sucesso')
                }
            })
            .catch(function (error) {
                console.log('erro')
            })
        ;
    }else{
        alert('Preencha todos os dados')
    }
}