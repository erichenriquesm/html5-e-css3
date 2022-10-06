<?php
include 'banco.php';
$nome = $_POST['nome'];
$email = $_POST['email'];
$senha = $_POST['senha'];
$dados = "INSERT INTO clientes VALUES('', '$nome', '$email', '$senha')";
$inserir = mysqli_query($database ,$dados);
echo "<script>
alert('Cadastro efetuado!')
window.location.href='lista.php'
</script>";
?>
