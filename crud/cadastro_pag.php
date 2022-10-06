<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="estilos/login/style.css">
    <link rel="stylesheet" href="estilos/login/media.css">
    <script src="../mascara.js"></script>
    <title>Cadastro</title>
</head>

<body>
    <section>

        <div>
            <h1>Cadastre-<span>se</span></h1>

            <div>
                <h3><a href="index.php">Home</a></h2> 
                      
            </div>

        </div>

    </section>

    <main>
        <h2>
            Cadastre e veja nossas receitas :)
        </h2>


        <form action="efetuar_cadastro.php" method="post">
            <label for="nome">Nome</label>
            <div>
                <input type="text" name="nome" id="nome" placeholder="Digite seu nome">
            </div>
            <label for="email">Email</label>
            <div>
                <input required type="email" name="email" id="email" placeholder="Digite seu email">
            </div>

            <label for="senha">Senha</label>
            <div>
                <input type="password" name="senha" id="senha" placeholder="Digite sua senha">
            </div>

            <input id="sub" type="submit" value="Cadastrar">
        </form>
    </main>

    <footer>
        <p><strong>&copy Todos os direitos reservados</strong></p>

            <div class="redes">

            <img class="icons"
                src="https://iconape.com/wp-content/files/yd/367773/svg/logo-linkedin-logo-icon-png-svg.png"
                alt="linkedin">

            <img class="icons"
                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlxt-AsCiNUxUA_RSkSKpx9MLRxIyW42rG3A&usqp=CAU"
                alt="instagram">
        </div>
    </footer>
</body>

</html>