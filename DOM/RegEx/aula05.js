const alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnoprstuvwxyz! @ 0123456789';

// [] conjunto é entre conchetes
//[abc]  el encontra apenas os conjunto a, b e c
//[] conjunto a ser achado
//[^] negar o que estiver no cunjunto a ser achado
//range [-] de alguma coisa até alguma cois do menor ao maior ex: [0-9]de 0 a 9, [9-0] NÃO
console.log(alfabeto)
console.log(alfabeto.match(/[0-9]+/gi))
console.log(alfabeto.match(/[a-z]+/gi))
console.log(alfabeto.match(/[a-z A-Z 0-9ãç]+/g)) //negação de tudo menos símbolos //unicode

//shrothand [a-z A-Z 0-9] = \w

console.log(alfabeto.match(/\w+/g))

//negação em shorthand são as letras em maiúsculas
console.log(alfabeto.match(/\W+/g)) // = [^a-z A-Z 0-9]

//conjunto de 0 a 9 = \d
console.log(alfabeto.match(/\d+/g))

//negação de 0 a 9 = \D
console.log(alfabeto.match(/\D+/g))

//mostrar todos os espaços dentro de uma string \s
console.log(alfabeto.match(/\s/g))

//negar os espaços \S

console.log(alfabeto.match(/\S+/g))

//[min - max qualquer outra coisa] [^min - max qualquer coisa] -> tudo menos isso