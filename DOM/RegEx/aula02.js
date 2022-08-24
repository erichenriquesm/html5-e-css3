const txt =  'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui laudantium deleniti voluptatibus nostrum vitae iure velit? Voluptas voluptates maxime iusto perferendis autem ratione rem exercitationem culpa fugiat, ad enim! Similique!Lore Lorem ipsum dolor sit, amet consectetur adipisicing elit. Corrupti consequuntur facere incidunt molestias a esse enim quaerat? Officia, impedit magnam eum recusandae blanditiis sapiente adipisci, cum veritatis ad non minus.';

//difernte do .exec, o comando .match é ao contrário = txt.match(RegWx)
//.replace(/valor a ser trocado/, valor novo) não altera o original
//No replace, você pode adicionar caracteres usando cifrao $ como grupo ou
/*Uma functiom txt.replace("Eric", function(valor a ser achado){
    console.log(valor a ser achado)
})*/


console.log(txt.replace(/ipsum/gi, function(input){ 
    return input.toUpperCase()
}));



