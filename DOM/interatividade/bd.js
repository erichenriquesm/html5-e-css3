let criarPerfil = (img, nome, des, fundo) => {
    return {
        img,
        nome,
        des,
        fundo
    }
}; 


function mostrarPerfil(link, nome, des, fundo){
    let img = document.querySelector('#img');
    img.setAttribute('src', link);

    let usuario = document.querySelector('#nome');
    usuario.innerText = nome;

    let descricao = document.querySelector('#des');
    descricao.innerText = des;

    document.body.style.backgroundImage = `url(${fundo})`
};

function per1(){

    let perfil1 = criarPerfil('per1/user.png', 'Eric', 'Olá, sou criador deste site em que mostro um pouco de HTML5, CSS3 E JavaScript utilizando domínio de objetos para deixar todas as informações dinâmicas. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Soluta fugit, sunt natus eveniet voluptas officiis quod. Similique, sed amet expedita quibusdam nisi quasi ab unde enim neque! Cupiditate, expedita obcaecati?', 'https://marquesfernandes.com/wp-content/uploads/2020/01/1555172-768x432.jpg')


    let fields = document.querySelectorAll('fieldset')
    fields.forEach((field) =>{ 
    field.style.color = 'yellow'
    field.style.border = '1px solid yellow '
});

    let usuario = document.querySelector('#nome');
    usuario.style.color = 'yellow';

    let des = document.querySelector('#des')
    des.style.color =  'yellow';
    
    mostrarPerfil(perfil1.img, perfil1.nome, perfil1.des, perfil1.fundo);

};

function per2(){
    let perfil2 = criarPerfil('per2/user.png', 'Leonardo', 'Olá, sou Leonardo, gosto de Star Wars e hoje estou dentro do projeto do meu amigo, espero que gostem. ectetur adipisicing elit. Soluta fugit, sunt natus eveniet voluptas officiis quod. Similique, sed amet expedita quibusdam nisi quasi ab unde enim neque! Cupiditate,ectetur adipisicing elit. Soluta fugit, sunt natus eveniet voluptas officiis quod. Similique, sed amet expedita quibusdam nisi quasi ab unde enim neque! Cupiditate,', 'https://mcdn.wallpapersafari.com/medium/38/65/Fcx7LA.jpg');

    let fields = document.querySelectorAll('fieldset')
    fields.forEach((field) =>{ 
    field.style.color = 'purple'
    field.style.border = '1px solid purple'
});

    let usuario = document.querySelector('#nome');
    usuario.style.color = 'purple';

    let des = document.querySelector('#des')
    des.style.color =  'purple';


    mostrarPerfil(perfil2.img, perfil2.nome, perfil2.des, perfil2.fundo);
};

function per3(){

    let perfil3 = criarPerfil('per3/user (2).jpeg', 'Yasmim', 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Soluta fugit, sunt natus eveniet voluptas officiis quod. Similique, sed amet expedita quibusdam nisi quasi ab unde enim neque! Cupiditate, expedita obcaecati?', 'per3/back.png')


    let fields = document.querySelectorAll('fieldset')
    fields.forEach((field) =>{ 
    field.style.color = '#E515A7'
    field.style.border = '1px solid #E515A7 '
});

    let usuario = document.querySelector('#nome');
    usuario.style.color = '#E515A7';

    let des = document.querySelector('#des')
    des.style.color =  '#E515A7';
    
    mostrarPerfil(perfil3.img, perfil3.nome, perfil3.des, perfil3.fundo)

};
