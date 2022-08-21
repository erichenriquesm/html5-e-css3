const ajax = new XMLHttpRequest();

ajax.open("GET", "https://github.com/erichenriquesm/html5-e-css3/blob/main/DOM/jsons/anime.json");

ajax.send();

ajax.onload = function (){
    let p = document.querySelector("p");
    p.innerHTML = this.responseText;
}