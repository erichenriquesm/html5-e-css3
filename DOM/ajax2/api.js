const ajax = new XMLHttpRequest();

ajax.open("GET", "http://localhost:3000/filmes");

ajax.send();

ajax.onload = function (){
    let p = document.querySelector("p");
    p.innerHTML = JSON.stringify(this.responseText);

}
