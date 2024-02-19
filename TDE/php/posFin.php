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
                    <a href="atvComp.php"><li>&nbsp;ATIVIDADES &nbsp;COMPLEMENTARES</li></a>
                    <a href="posFin.php"><li class="sideSelect">&nbsp;POSIÇÃO &nbsp;FINANCEIRA</li></a>
                </ul>
            </nav>
        </div>
        
        
        <div class="containerPOS" >


            <div class="tabelinhasui">
                <div class="semestre">
                    <h4>1º SEMESTRE</h4>
                </div>
                <div class="semestre">
                    <h4>2º SEMESTRE</h4>
                </div>
            </div>
            
            <div class="tabelinhasui">
                
                
                <!-- PRIMEIRO SEMESTRE-->
                
                <table class="posBox" id="sem1">

                    <thead>
                        <tr class="atvHeader">
                            <td><h4>Vencimento</h4></td>
                            <td><h4>Valor</h4></td>
                            <td><h4>Imprimir</h4></td>
                            <td><h4>Status</h4></td>
                        </tr>
                    </thead>

                    <tbody>
                        <tr class="atv">
                            <td><p>06/01/2023</p></td>
                            <td><p>R$2.050,00</p></td>
                            <td><img src="../images/comprovante.png" width="30px"></td>
                            <td><p>Pago</p></td>
                        </tr>
                        
                        <tr class="atv">
                            <td><p>06/02/2023</p></td>
                            <td><p>R$2.050,00</p></td>
                            <td><img src="../images/comprovante.png" width="30px"></td>
                            <td><p>Pago</p></td>
                        </tr>

                        <tr class="atv">
                            <td><p>06/03/2023</p></td>
                            <td><p>R$2.050,00</p></td>
                            <td><img src="../images/comprovante.png" width="30px"></td>
                            <td><p>Pago</p></td>
                        </tr>
                        
                        <tr class="atv">
                            <td><p>06/04/2023</p></td>
                            <td><p>R$2.050,00</p></td>
                            <td><img src="../images/comprovante.png" width="30px"></td>
                            <td><p>Pago</p></td>
                        </tr>
                        
                        
                        <tr class="atv">
                            <td><p>06/05/2023</p></td>
                            <td><p>R$2.050,00</p></td>
                            <td><img src="../images/comprovante.png" width="30px"></td>
                            <td><p>Pago</p></td>
                        </tr>
                        
                        <tr class="atv">
                            <td><p>06/06/2023</p></td>
                            <td><p>R$2.050,00</p></td>
                            <td><img src="../images/comprovante.png" width="30px"></td>
                            <td><p>Pago</p>
                        </tr>
                    </tbody>
                        
                    <tfoot>
                        <tr class="atvFooter">
                            <td>&nbsp;</td>
                        </tr>
                    </tfoot>
                </table>

                <!-- 2º SEMESTRE -->
                <table class="posBox" id="sem2">

                    <thead>
                        <tr class="atvHeader">
                            <td><h4>Vencimento</h4></td>
                            <td><h4>Valor</h4></td>
                            <td><h4>Imprimir</h4></td>
                            <td><h4>Status</h4></td>
                        </tr>
                    </thead>

                    <tbody>
                        
                        <tr class="atv">
                            <td><p>06/07/2023</p></td>
                            <td><p>R$2.050,00</p></td>
                            <td><img src="../images/comprovante.png" width="30px"></td>
                            <td><p>Pago</p></td>
                        </tr>

                        <tr class="atv">
                            <td><p>06/08/2023</p></td>
                            <td><p>R$2.050,00</p></td>
                            <td><img src="../images/comprovante.png" width="30px"></td>
                            <td><p>Pago</p></td>
                        </tr>
                        
                        <tr class="atv">
                            <td><p>06/09/2023</p></td>
                            <td><p>R$2.050,00</p></td>
                            <td><img src="../images/comprovante.png" width="30px"></td>
                            <td><p>Pago</p></td>
                        </tr>
                        
                        
                        <tr class="atv">
                            <td><p>06/10/2023</p></td>
                            <td><p>R$2.050,00</p></td>
                            <td><img src="../images/comprovante.png" width="30px"></td>
                            <td><p>Pago</p></td>
                        </tr>
                        
                        <tr class="atv">
                            <td><p>06/11/2023</p></td>
                            <td><p>R$2.050,00</p></td>
                            <td><img src="../images/comprovante.png" width="30px"></td>
                            <td><p>Pago</p></td>
                        </tr>

                        <tr class="atv" style="padding: 20px;">
                            <td><p>06/12/2023</p></td>
                            <td><p>R$2.050,00</p></td>
                            <td><img src="../images/impressora.png" width="20.2px"></td>
                            <td><p>Em espera</p></td>
                        </tr>

                    </tbody>
                    
                    <tfoot>
                        <tr class="atvFooter">
                            <td></td>
                        </tr>
                    </tfoot>
                    
                </table>
            </div>
        </div>

    </main>

    <footer >
        <p>Todos os direitos reservados e coisarada</p>
    </footer>
</body>
</html>