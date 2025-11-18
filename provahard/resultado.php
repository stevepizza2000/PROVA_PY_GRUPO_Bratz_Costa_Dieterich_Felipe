<?php
$host = "localhost"; 
$user = "root";
$pass = "";
$bd   = "db_logistica";

$conec = new mysqli($host, $user, $pass, $bd);
if ($conec->connect_error) {
    die("Erro de conexão: " . $conec->connect_error);
}

if (!isset($_GET['codigo'])) {
    die("Código não informado!");
}

$codigo = $_GET['codigo'];

$stmt = $conec->prepare("SELECT * FROM tb_envios WHERE codigo = ?");
$stmt->bind_param("i", $codigo);
$stmt->execute();
$resultado = $stmt->get_result();

if ($resultado->num_rows == 0) {
    die("Código não encontrado!");
}

$dados = $resultado->fetch_assoc();
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title>Resultado do Rastreio</title>
	<link rel="stylesheet" href="css/estilo2.css"
</head>
<body>

<h1>Resultado do Rastreio</h1>

<p><strong>Código:</strong> <?PHP echo $dados["codigo"] ?></p>
<p><strong>Descrição:</strong> <?PHP echo $dados["descricao"] ?></p>
<p><strong>Status:</strong> <?PHP echo $dados["condicao"] ?></p>
<p><strong>Localização:</strong> <?PHP echo $dados["localizacao"] ?></p>

<a href="index.php">Voltar</a>

</body>