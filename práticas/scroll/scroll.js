const blocos = document.querySelectorAll('[data-animation]');
const classe = 'mostrar';

function exibir(){
    const topo = window.pageYOffset;
    blocos.forEach(function(bloco){
        if(topo > bloco.offsetTop -300){
            bloco.classList.add(classe);
        }else{
            bloco.classList.remove(classe);
        }
    });
}


 window.addEventListener("scroll", function(){
    exibir();
})
