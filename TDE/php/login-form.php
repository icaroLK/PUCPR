<!DOCTYPE html>
<html lang="en">
<head> 
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/login.css">
	<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet" />
    <title>Universe</title>
</head>
<body>

<?php
require_once 'funcoes.php';



?>

<img src="../images/UniverseVermelho.png" style="width: 20vw; margin: 10px; padding: 0;">
<div class="container" id="container">
	<div class="form-container sign-up-container">
		<form action="#">
			<h1>Professor</h1>
			<div class="social-container">
				<img src="../images/microsoft.png" class="social"><i class="fab fa-linkedin-in"></i></img>
			</div>
			<span>ou acesse sua conta atraves do E-mail</span>
			<input type="text" placeholder="Nome" />
			<input type="email" placeholder="Email" />
			<input type="password" placeholder="Senha" />
			<button><a href="home.php">Entrar</a></button>
		</form>
	</div>
	<div class="form-container sign-in-container">
        <form action="index.php" method="post">
			<h1>Aluno</h1>
			<div class="social-container">
				<img src="../images/microsoft.png" class="social"><i class="fab fa-linkedin-in"></i></img>
			</div>
			<span>ou acesse sua conta atraves do E-mail</span>
			<input type="email" placeholder="Email" required name="email" />
			<input type="password" placeholder="Senha" required name="senha" />
			<a href="#">Esqueceu sua senha?</a>
            <input type="submit" value="ENTRAR" style="background-color: #A43039; color: white; border-radius: 30px; font-weight: bold; width: 150px;">
		</form>

	</div>
	<div class="overlay-container">
		<div class="overlay">
			<div class="overlay-panel overlay-left">
				<h1>Olá Professor!</h1>
				<p>Venha ampliar o conhecimentos de nossos alunos!</p>
				<button class="ghost" id="signIn">Sou aluno</button>
			</div>
			<div class="overlay-panel overlay-right">
				<h1>Olá, Aluno!</h1>
				<p>Venha ampliar o conhecimento com a UniVerse!</p>
				<button class="ghost" id="signUp">Sou professor</button>
			</div>
		</div>
	</div>


</div>
</body>


<script>
    const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});
 </script>
</html>