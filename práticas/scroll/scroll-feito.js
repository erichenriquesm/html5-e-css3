const blocos = document.querySelectorAll('[data-animation]');
const classe = 'mostrar';

function exibir(){
    //verificar a distancia do scroll e o topo do site
    const topoDoSite = window.pageYOffset; // pegar a localização do scroll até o topo da pagina
    //para cada bloco precisamos pegar a localoização do eixo y
    blocos.forEach(function(bloco){
        if(topoDoSite > bloco.offsetTop -300){
            bloco.classList.add(classe);
        }else{
            bloco.classList.remove(classe);
        } //usar o elemento.offsetTop para pegar a localização
    });
}

exibir();

if(blocos.length){
    window.addEventListener("scroll", function(){
        exibir();
        console.log('ababadi')
    });
}