const txt =  'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui laudantium deleniti voluptatibus nostrum vitae iure velit? Voluptas voluptates maxime iusto perferendis autem ratione rem exercitationem culpa fugiat, ad enim! Similique!Lore Lorem ipsum dolor sit, amet consectetur adipisicing elit. Corrupti consequuntur facere incidunt molestias a esse enim quaerat? Officia, impedit magnam eum recusandae blanditiis sapiente adipisci, looooooooooooooooremmmmmmmmmmmmmmmmmmmmmm cum veritatis ad non minus.';

// quantificador * (opcionais) 0 ou mais vezes{0,}
//quantificador + (obrigatório) 1 ou mais vezes{1,}
//quantificador ? (opcionais) 0 ou uma vezes{0, 1}

// console.log(txt);

// const regEx = /lo+rem+/gi;
// //1 o ou mais
// //1m ou mais
// console.log(txt.match(regEx));
// \ é literal exemplo \for
//{min, max} minimo e maximo
//{10,} no minimo 10
//{, 10} de 0 a 10
//{10} tem que ser 10

const arquivos = ['atencao.jpg', 'foto.jpg', 'meu gatinho.jpeg', 'marido.png', 'lista de compras.txt']

const regEx = /\.jpe{0,1}g/gi
//o "e" pode aparecer 1 vez ou não ?

arquivos.forEach((arquivo) =>{
    let valido = arquivo.match(regEx);
    if(valido){
        console.log(arquivo, arquivo.match(regEx))
    }
    
})