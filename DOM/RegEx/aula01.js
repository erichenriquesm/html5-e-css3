const txt =  'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui laudantium deleniti voluptatibus nostrum vitae iure velit? Voluptas voluptates maxime iusto perferendis autem ratione rem exercitationem culpa fugiat, ad enim! Similique!Lore Lorem ipsum dolor sit, amet consectetur adipisicing elit. Corrupti consequuntur facere incidunt molestias a esse enim quaerat? Officia, impedit magnam eum recusandae blanditiis sapiente adipisci, cum veritatis ad non minus.';

//RegEx
//g - global(todas as ocorrências)
//i - insensity(refuta letras maiúsculas e minúsculas)
//.test me traz se a palavra que está na variável de reg é verdadeira ou falsa
//.exec me traz o texto em objeto e se a resposta não for null, ele me traz a resposta no índice[0]
//exec.input me traz todo o texto
//() grupo me traz (ola)(mundo) podendo me resultar em "ola", "mundo" ou "ola mundo"

const regEx = /(lorem) (ipsum)/gi;

console.log(regEx.test(txt))

console.log(regEx.exec(txt))