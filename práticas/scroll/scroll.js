let blocos = document.querySelectorAll('[data-animation]');
let mostrar = 'mostrar';

function exibir(){
    blocos.forEach(bloco =>{
        let siteTop = window.pageYOffset;
        if(siteTop > bloco.offsetTop - 300){
            bloco.classList.add(mostrar);
        }else{
            bloco.classList.remove(mostrar);
        }
    })
}   

exibir();

if(blocos.length > 0){
    window.addEventListener('scroll', function(){
        exibir();
    })
}