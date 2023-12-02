<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/style.css">
    <script src="../js/javascript.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet" />
    <title>UniVerse</title>
</head>
<body class="princ">

<?php
require_once 'funcoes.php';

?>
    <header>
        <img src="../images/UniverseBranco.png" alt="">

        <div class="perfil">
            <?php
            if(!($_SESSION['usuario'])){
                echo 'entrar';
            }else{

                echo "<div class='perfil'>Olá, " . $_SESSION['nome'] . "</div>";
                echo '<a href="index.php?logout=1"><p class="logout">Sair</p></a>';
            }
            ?>
        </div>
    </header>

    <main>
        <div class="sideNav">
            <nav>
                <ul>
                    <a href="home.php"><li>&nbsp;HOME</li></a>
                    <a href="aulas.php"><li class="sideSelect">&nbsp;MINHAS AULAS</li></a>
                    <a href="notas.php"><li>&nbsp;NOTAS/<br>&nbspFREQUÊNCIA</li></a>
                    <a href="atvComp.php"><li>&nbsp;ATIVIDADES &nbsp;COMPLEMENTARES</li></a>
                    <a href="posFin.php"><li>&nbsp;POSIÇÃO &nbsp;FINANCEIRA</li></a>
                </ul>
            </nav>
        </div>

        <div class="containerN">
            <table class="notas">
            <?php
                    // $pesq = $banco->query("select * from materias;");



                    $nomeatual = $_SESSION['nome'];
                    // echo $nomeatual;
                    $pesq = $banco->query("Select mu.id, u.nome, m.materia, mu.frequencia, mu.nota, m.carga FROM materia_usuario AS mu 
                                            INNER JOIN usuarios AS u ON (mu.id_usuario = u.id)
                                            INNER JOIN materias AS m ON (mu.id_materia = m.id)
                                            WHERE u.nome LIKE '$nomeatual'");





                    $qtdLinha = $pesq->num_rows;
                    
                    echo "<thead>";
                        echo "<tr>";
                            echo "<th><h1>Matérias</h1></th>";
                            echo "<th><h1>Carga horária</h1></th>";
                        echo "<tr>";
                    echo "</thead>";

                    
                
                    echo "<tbody>";
                    for($i = 1; $i <= $qtdLinha; $i++){

                        $objAtual = $pesq->fetch_object();
                        // print_r($objAtual);
                       

                        echo "<tr>";
                           echo "<td>$objAtual->materia</td>";
                           echo "<td>$objAtual->carga</td>";
                        echo "</tr>";

                    };
                    echo "</tbody>";
                
                ?>
            </table>
        </div>
    </main>

    <footer >
        <p>Todos os direitos reservados e coisarada</p>
    </footer>
</body>
</html>