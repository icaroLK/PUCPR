<!DOCTYPE html>
<html lang="en">
<head> 
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/login.css">
	<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet" />
    <title>Universe</title>
	<style>

div.msg {
    padding: 7px 15px;
    margin-bottom: 15px;
    border-radius: 15px;
    background-color: rgba(226, 239, 218);
}

div.sucesso {
    color: rgba(74, 116, 67);
}

div.aviso {
    color: rgb(88, 104, 29);
}

div.erro {
    color: rgb(138, 53, 53);
}


a {
	color: black;
}


	</style>
</head>
<body>

<?php
require_once 'funcoes.php';


?>



<?php

$log = $_GET['logout'] ?? null;

if($log == 1){
	logout();
}


$em = $_POST['email'] ?? null;
$sen = $_POST['senha'] ?? null;


// $em = 'icarolkucha@gmail.com';
// $sen = "senhaaaforte";



if($em == null || $sen == null){
	require 'login-form.php';
}else{

	$q = "Select usuario, nome, email, senha, tipo from usuarios where email = '$em'";
	$busca = $banco->query($q);
	if(!$busca){
		echo msg_erro('Erro ao acessar o banco');
	}else{
		$objAtual = $busca->fetch_object();
		
		
		if($objAtual == null){
			
			echo msg_erro('Usuário não encontrado');
		}else{
			if(!($sen === $objAtual->senha)){
				echo msg_erro('Senha errada');
			}else{
				$_SESSION['usuario'] = $objAtual->usuario;
				$_SESSION['nome'] = $objAtual->nome;
				$_SESSION['email'] = $objAtual->email;
				$_SESSION['tipo'] = $objAtual->tipo;
				echo msg_sucesso('Logado com sucesso');
				echo "<p><a href='home.php'>Clique aqui para acessar a home</a></p>";
			}
		}
	}
}




?>


</body>

</html>