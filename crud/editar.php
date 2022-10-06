<?php
include 'banco.php';
$id = $_POST['id'];
$email = $_POST['email'];
$nome = $_POST['nome'];
$senha = $_POST['senha'];
$table = 'SELECT * FROM clientes';
$table_request = mysqli_query($database, $table);
while($obter = mysqli_fetch_array($table_request)){
    if(strlen($email) == 0 || strlen($nome) == 0 || strlen($senha) == 0){
        echo "<script>
        alert('Algum dado está vazio!')
        window.location.href='edicao.php'
        </script>";
    }else{
        $dados = "UPDATE clientes SET email = '$email', nome = '$nome', senha = '$senha' WHERE id = '$id'";
        $atualizar = mysqli_query($database, $dados);
        echo "<script>
        alert('Edição feita!')
        window.location.href='lista.php'
        </script>";
    }
}

?>