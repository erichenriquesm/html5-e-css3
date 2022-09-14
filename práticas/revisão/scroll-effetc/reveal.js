const blocos = document.querySelectorAll('[data-animate]');

function exibir(){
    const topo = window.pageYOffset;
    blocos.forEach(bloco =>{
        if(topo > bloco.offsetTop - 400){
            bloco.classList.add('reveal')
        }else{
            bloco.classList.remove('reveal')
        }
    })
}

exibir();

if(blocos.length){
    window.addEventListener('scroll', () =>{
        exibir();
    })
}