//<.+> .+ <\/.+> . representa qualquer caractere que não quebre linha .* 0 caracteres ou mais .+ 1 ou mais caracteres .? 0 ou 1 caractere
// \ para que a barra(/) escape para o sentido literal

const html = '<p>Olá mundo</p> <p>Olá de novo</p>';
console.log(html.match(/<.+>.+<\/.+>/gi)); //greedy - guloso ir até onde der
console.log(html.match(/<.+?>.+?<\/.+?>/gi)); // non greedy - vai até no minimo q der