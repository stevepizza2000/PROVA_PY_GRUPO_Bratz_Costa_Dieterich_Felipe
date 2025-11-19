<?php
//conexão com banco de dados
$host = "localhost"; 
$user = "root";
$pass = "";
$bd   = "db_logistica";

$conec = new mysqli($host, $user, $pass, $bd);
if ($conec->connect_error) {
    die("Erro de conexão: " . $conec->connect_error);
}

//verifica se o código foi enviado
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $codigo = $_POST["codigo"]; //recebe o código digitado

//prepara uma consulta segura
    $stmt = $conec->prepare("SELECT localizacao FROM tb_envios WHERE codigo = ?");
    $stmt->bind_param("i", $codigo);
    $stmt->execute();
    $resultado = $stmt->get_result();

//verifica se encontrou algum registro (codigo)
	if ($resultado->num_rows > 0) {

// redireciona para a segunda página
		header("Location: resultado.php?codigo=$codigo");
		exit();

	} else {
		$erro = "Código não encontrado!";
	}
}
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title>Consulta de Rastreio</title>
    <link rel="stylesheet" href="static/estilo.css">
</head>

<body>
    <div id="caixa">
        <h1>Consulta de Rastreio</h1>

        <p>Insira o código de rastreio para ver o status do envio. Não é necessário login.</p>

        <form method="POST">
            <label for="codigo">Código de Rastreio:</label>
            <input id="codigo" name="codigo" type="number" placeholder="EX: 1234567891" required>
            <button type="submit">Consultar</button>
        </form>


    </div>
</body>
