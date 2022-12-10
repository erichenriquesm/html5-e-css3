const blocos = document.querySelectorAll('[data-animation]');

function exibir(){
    const topoDoSite = window.pageYOffset;
    blocos.forEach(bloco =>{
        if(topoDoSite > bloco.offsetTop - 300){
            bloco.classList.add('mostrar');
            return;
        }
        bloco.classList.remove('mostrar');

    });
}

exibir();

if(blocos.length){
    window.addEventListener('scroll', () =>{
        exibir();
    })
}