// const txt =  'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui laudantium deleniti voluptatibus nostrum vitae iure velit? Voluptas voluptates maxime iusto perferendis autem ratione rem exercitationem culpa fugiat, ad enim! Similique!Lore Lorem ipsum dolor sit, amet consectetur adipisicing elit. Corrupti consequuntur facere incidunt molestias a esse enim quaerat? Officia, impedit magnam eum recusandae blanditiis sapiente adipisci, cum veritatis ad non minus.';

// const regEx = /dolor/gi;

// console.log(regEx.test(txt));
// console.log(regEx.exec(txt));
// console.log(txt.match(regEx));
// console.log(txt.replace(/dolor/gi, "AINNNNN"))


const frase = 'Um dia, a raposa leu pro raposo';

console.log(frase.replace(/(um) (raposa)/gi, '<$1>'))