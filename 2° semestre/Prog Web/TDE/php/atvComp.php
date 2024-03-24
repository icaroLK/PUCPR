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
ob_start()

?>
    <header>
        <img src="../images/UniverseBranco.png" alt="">

        <div class="perfil">
            <?php
            if(!($_SESSION['usuario'])){
                echo 'entrar';
            }else{

                echo "<div class='perfil'>Olá, " . $_SESSION['nome'] . "</div>";
                echo '<p class="logout"><a href="index.php?logout=1">Sair</a></p>';
            }
            ?>
        </div>
    </header>

    <main>

        <div class="sideNav">
            <nav>
                <ul>
                    <a href="home.php"><li>&nbsp;HOME</li></a>
                    <a href="aulas.php"><li>&nbsp;MINHAS AULAS</li></a>
                    <a href="notas.php"><li>&nbsp;NOTAS/<br>&nbspFREQUÊNCIA</li></a>
                    <a href="atvComp.php"><li class="sideSelect">&nbsp;ATIVIDADES &nbsp;COMPLEMENTARES</li></a>
                    <a href="posFin.php"><li>&nbsp;POSIÇÃO &nbsp;FINANCEIRA</li></a>
                </ul>
            </nav>
        </div>

        <div class="barra">
            <div class="progresso">
                
            </div>
        </div>
        <h2 class="horas">0%</h2>

        <!-- MEUS -->
        <div class="containerATV pagina" id="idATVM">

            <div class="navATV">
                <nav>
                    <ul>
                        <a><li class="homeSelect">MINHAS ATIVIDADES</li></a>
                        <a onclick="some('idATVM'), showPage('idATVE')"><li>ENVIAR ATIVIDADE</li></a>
                        <a onclick="some('idATVM'), showPage('idATVD')"><li>DELETAR ATIVIDADE</li></a>
                    </ul>
                </nav>
            </div>

            <table class="atvBox">
                
                <?php
                    $nomeatual = $_SESSION['nome'];
                    $pesq = $banco->query(" Select a.id, a.nome, a.grupo, a.tipo, a.horas, a.posicao from atividade AS a
                    INNER JOIN usuarios AS u ON (a.fk_id_usuario = u.id)
                    WHERE u.nome LIKE '$nomeatual'
                    ORDER BY a.nome");
                    
                    
                    
                    echo "<thead>";
                    echo "<tr class='atvHeader'>";
                    echo "<td><h4>ID</h4></td>";
                    echo "<td><h4>Nome</h4></td>";
                    echo "<td><h4>Instituição</h4></td>";
                    echo "<td><h4>Tipo</h4></td>";
                    echo "<td><h4>Horas</h4></td>";
                    echo "<td><h4>Status</h4></td>";
                    echo "<tr>";
                    echo "</thead>";
                    
                    
                    $qtdLinha = $pesq->num_rows;
                    if($qtdLinha != 0){
                    
                        echo "<tbody>";
                        for($i = 1; $i <= $qtdLinha; $i++){
                            
                            $objAtual = $pesq->fetch_object();
                            
                            
                            echo "<tr class='atv'>";
                            echo "<td>$objAtual->id</td>";
                            echo "<td>$objAtual->nome</td>";
                            echo "<td>$objAtual->grupo</td>";
                            echo "<td>$objAtual->tipo</td>";
                            echo "<td>$objAtual->horas</td>";
                            echo "<td>$objAtual->posicao</td>";
                            echo "</tr>";
                            
                        };
                        echo "</tbody>";
                    }else {
                        echo "<tr class='atv'>";
                        echo "<td colspan='6'>Voce ainda não inseriu nenhuma atividade complementar</td>";
                        echo "</tr>";
                    }
                    
                    ?>
                    <tfoot>
                        <tr class="atvFooter">
                            <td>&nbsp;</td>
                        </tr>
                    </tfoot>

</table>            

</div>


<!-- ENVIAR -->       
<div class="subpagina containerATV" id="idATVE">
    
    <div class="navATV">
        <nav>
                    <ul>
                        <a onclick="showPage('idATVM')"><li>MINHAS ATIVIDADES</li></a>
                        <a><li class="homeSelect">ENVIAR ATIVIDADE</li></a>
                        <a onclick="showPage('idATVD')"><li>DELETAR ATIVIDADE</li></a>
                    </ul>
                </nav>
            </div>

            

            <form class="formFaculRides" action=<?php echo $_SERVER['PHP_SELF'];?> method="post">
                <div class="sem_nome">
                    <table class="atvBox">
                        <thead>
                            <tr class="atvHeader">
                                <td><h4>Nome</h4></td>
                                <td><h4>Grupo</h4></td>
                                <td><h4>Tipo</h4></td>
                                <td><h4>Horas</h4></td>
                                <td><h4></h4></td>
                            </tr>
                        </thead>
                        
                        <tr class="atv">
                            <!-- ID INT PRIMARY KEY AUTO INCREMENT -->
                            <td><input type="text" class="input_atv" name="nomeatv" required></td>
                            <td><input type="text" class="input_atv" name="grupoatv" required></td>
                            <!-- <td><input type="text" class="input_atv" name="tipoatv" required></td> -->
                            <td>
                                <select name="tipoatv" id="idtipo" class="input_atv" required>
                                    <option value="--"></option>
                                    <option value="palestra">Palestra</option>
                                    <option value="Workshop">Workshop</option>
                                    <option value="tv">Trabalho Voluntário</option>
                                </select>
                             </td>
                            <td><input type="number" class="input_atv" name="horasatv" required></td>
                        </tr>


                        <tfoot>
                            <tr class="atvFooter">
                                <td>&nbsp;</td>
                            </tr>
                        </tfoot>
                    </table>

                    <table class="atvBoxComp">
                        <thead>
                            <tr class="atvHeader">
                                <td><h4>Comprovante</h4></td>
                            </tr>
                        </thead>

                        <tr class="atv">
                            <td><input type="file"></td>
                        </tr>

                        <tfoot>
                            <tr class="atvFooter">
                                <td>&nbsp;</td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
                
                  <button class="atvSubmit" type="submit" name="atvSub" id="idatvSub">Enviar</button>  

                

                   
            <?php

                    $nomeatv = $_POST['nomeatv'] ?? null;
                    $grupoatv = $_POST['grupoatv'] ?? null;
                    $tipoatv = $_POST['tipoatv'] ?? null;
                    $horasatv = $_POST['horasatv'] ?? null;
                    
                    if($nomeatv !== null && $grupoatv !== null && $tipoatv !== null && $horasatv !== null){
                        
                        $nomeatual = $_SESSION['nome'];
                        $idAtual = $banco->query("Select id from usuarios WHERE nome LIKE '$nomeatual'")->fetch_object()->id;
                        
                        
                        $banco->query("Insert into atividade(nome, grupo, tipo, horas, posicao, fk_id_usuario) VALUES
                        ('$nomeatv', '$grupoatv', '$tipoatv', $horasatv, 'Em Análise', $idAtual)");
                        
                        
                        
                        $_POST['nomeatv'] = null;
                        $_POST['grupoatv'] = null;
                        $_POST['tipoatv'] = null;
                        $_POST['horasatv'] = null;

                        header('Location: atvComp.php');
                        exit;
                    }

            
            ?>
                
            </form>
            
        





        </div>


        <!-- DELETAR -->
        <div class="subpagina containerATV" id="idATVD">

            <div class="navATV">
                <nav>
                    <ul>
                        <a onclick="showPage('idATVM')"><li>MINHAS ATIVIDADES</li></a>
                        <a onclick="showPage('idATVE')"><li>ENVIAR ATIVIDADE</li></a>
                        <a><li class="homeSelect">DELETAR ATIVIDADE</li></a>
                    </ul>
                </nav>
            </div>

            <form class="formFaculRides" action=<?php echo $_SERVER['PHP_SELF'];?> method="post">
                <table class="atvBox">
                    <thead>
                        <tr class="atvHeader">
                            <td><h4>ID da Atividade</h4></td>
                            <td><h4>Motivo</h4></td>
                            <td><h4>Confirmar</h4></td>
                        </tr>
                    </thead>
                    
                    <tr class="atv">
                        <!-- ID INT PRIMARY KEY AUTO INCREMENT -->
                        <td><input type="number" class="input_atv" name="idatv" required></td>
                        <td><input type="text" class="input_atv" required></td>
                        <td><input type="checkbox" class="anex" required></td>
                    </tr>

                    <tfoot>
                        <tr class="atvFooter">
                            <td>&nbsp;</td>
                        </tr>
                    </tfoot>
                </table>

                <input class="atvSubmit" type="submit" name="atvDel" id="idatvDel">
                <?php

                    $idatv = $_POST['idatv'] ?? null;
                    
                    if($idatv !== null){
                        
                        $nomeatual = $_SESSION['nome'];
                        $idAtual = $banco->query("Select id from usuarios WHERE nome LIKE '$nomeatual'")->fetch_object()->id;
                        
                        
                        $banco->query("Delete from atividade WHERE fk_id_usuario = $idAtual AND id = $idatv");

                        header('Location: atvComp.php');
                        exit;
                    }
            ?>
            </form>
        </div>
        


    </main>

    <footer >
        <p>Todos os direitos reservados e coisarada</p>
    </footer>
</body>
</html>