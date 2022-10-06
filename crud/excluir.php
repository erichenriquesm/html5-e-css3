<?php
include 'banco.php';
$id = $_POST['id'];
$dados = "DELETE FROM clientes WHERE id = '$id'";
$excluir = mysqli_query($database, $dados);
header('location: lista.php');
?>