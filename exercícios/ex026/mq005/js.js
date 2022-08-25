function mostrar(){
    let menu = document.querySelector('#menu');
    if(menu.style.display == 'block'){
        menu.style.display = 'none';
    }else{
        menu.style.display = 'block'
    }
}