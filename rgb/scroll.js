const blocos = document.querySelectorAll('[data-animation]');
const classe = 'mostrar';


function exibir(){
    const topoDoSite = window.pageYOffset;
    blocos.forEach(bloco =>{
        if(topoDoSite > bloco.offsetTop -300){
            bloco.classList.add(classe);
        }else{
            bloco.classList.remove(classe);
        }
    });
};


exibir();
if(blocos.length){
    window.addEventListener('scroll', function(){
        exibir();
    })
}