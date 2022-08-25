const cpfs = `
        Os CPFs são:
        254.224.877-45 215.978.456-12 047.258.369-96 963.987.321-00
`;

console.log(cpfs.match(/\d{3}\.\d{3}\.\d{3}-\d{2}/g));

console.log(cpfs.match(/(\d{3}\.){2}\d{3}-\d{2}/g)); // forma simplificada com grupo e ocorrências

const ips = `
os ips validos são: 
0.0.0.0
10.10.5.10
255.255.255.255`;

console.log(ips.match(/[0-255]+\.[0-255]+\.[0-255]+\.[0-255]+/g));

console.log(ips.match(/([0-255]+\.){3}[0-255]+/g)); //versão simplificada com grupos e ocorrências