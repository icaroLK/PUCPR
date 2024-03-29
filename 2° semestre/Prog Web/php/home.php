<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="..\css\style.css">
    <script src="..\js\javascript.js"></script>
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
        <!-- NAVEGAÇÃO LATERAL -->
        <div class="sideNav">
            <nav>
                <ul>
                    <a href="home.php"><li class="sideSelect">&nbsp;HOME</li></a>
                    <a href="aulas.php"><li>&nbsp;MINHAS AULAS</li></a>
                    <a href="notas.php"><li>&nbsp;NOTAS/<br>&nbspFREQUÊNCIA</li></a>
                    <a href="atvComp.php"><li>&nbsp;ATIVIDADES &nbsp;COMPLEMENTARES</li></a>
                    <a href="posFin.php"><li>&nbsp;POSIÇÃO &nbsp;FINANCEIRA</li></a>
                </ul>
            </nav>
        </div>


        <!-- HOME -->
        <div class="containerH" id="idHH">

            <div class="navHome">
                <nav>
                    <ul>
                        <a><li class="homeSelect">HOME</li></a>
                        <a onclick="showPage('idHA'), some('idHH')"><li>AVISOS</li></a>
                        <a onclick="showPage('idHF'), some('idHH')"><li>FACULRIDES</li></a>
                        <a onclick="showPage('idHE'), some('idHH')"><li>ESTÁGIOS</li></a>
                    </ul>
                </nav>
            </div>
            
            <div class="bemvindo">
                <h1>Sejam Bem-Vindos à UniVerse!</h1>
                <p>O mais completo WebAluno para todas as faculdades!</p>
            </div>

            <div class="boneco">
                <img width="200px" src="../images/boneco.png" alt="Olá, eu sou o Rubi!">
            </div>

            <div class="iconInsta">
                <img width="30px" src="../images/insta_icon.png" name="insta">
                <label for="insta">@universe.pjbl</label>
            </div>

        </div>


        <!-- AVISOS -->
        <div class="containerH subpagina" id="idHA">

            <div class="navHome">
                <nav>
                    <ul>
                        <a onclick="showPage('idHH')"><li>HOME</li></a>
                        <a><li class="homeSelect">AVISOS</li></a>
                        <a onclick="showPage('idHF')"><li>FACULRIDES</li></a>
                        <a onclick="showPage('idHE')"><li>ESTÁGIOS</li></a>
                    </ul>
                </nav>
            </div>

            <div class="aviso">
                <img src="../images/warning.png" width="70px" height="60px">
                <h1 class="textAviso">AVISOS</h1>
            </div>
        


            <div class="warnBox" onclick="revealTxt('aviso1')">
                
                <h3>Está com problemas? Entre em contato!<img src="../images/select_icon.png" width="30px" height="15px" style="margin-left: 510px;"></h3> 
                <p id="aviso1" style="margin-top: 15px; display: none;">
                    Estudante, caso você esteja com limitações de acesso ao WebAluno devido a pendência de documentos e um deles seja o Contrato de Prestação de Serviços Educacionais, orientamos que entre em contato conosco pelo Telefone: (41) 99999-9999 ou Whatsapp em https://universe.app/whatsapp-universe, após sua identificação, quando a Joelma perguntar <strong>"Sobre o que vamos conversar?"</strong> digite <strong>"Falar com Atendente"</strong> e solicite o seu contrato.
                </p>
            </div>

            <div class="warnBox" onclick="revealTxt('aviso2')"> 

                <h3>Não deixe de enviar os documentos necessários para a matrícula!<img src="../images/select_icon.png" width="30px" height="15px" style="margin-left: 282px;"></h3>
     
                <p id="aviso2" style="margin-top: 15px; display: none;">
                    Você já sabe, mas não custa relembrar! Para concluir sua matrícula, é imprescindível que você tenha realizado a entrega de todos os documentos. E caso ainda não tenha concluído essa parte - fica o aviso:
                    <br><br>
                    Os estudantes com documentos pendentes tem um prazo para concluir a entrega da documentação, você será notificado diariamente até a data limite para a entrega.
                    <br><br>
                    Atente-se ao prazo para regularizar esta etapa, pois após essa data você terá limitações de acesso.
                    <br><br>
                    Acesse o <strong>Menu > Entrega de Documentação</strong> e verifique se tem algum documento ainda pendente e/ou indeferido.
                </p>
            </div>

            <div class="warnBox" onclick="revealTxt('aviso3')">    
                
                <h3>Sobre a Carteirinha Virtual!<img src="../images/select_icon.png" width="30px" height="15px" style="margin-left: 627px;"></h3>
                
                <p id="aviso3" style="margin-top: 15px; display: none;">
                    Você sabia que pela </strong>UniVerse</strong>, você possui a carteirinha de estudante virtual? Esta é uma vantagem exclusiva para as nossas Universidades parceiras! Entretanto, caso você precise acessar os ambientes físicos do Campus, solicite sua carteirinha física por meio do protocolo <strong>WEB Aluno > Menu > Protocolos > Pós - 1ª via de carteirinha.</strong>
                </p>    
            </div>

        </div>


        <!-- FACULRIDES -->
        <div class="containerH subpagina" id="idHF">

            <div class="navHome">
                <nav>
                    <ul>
                        <a onclick="showPage('idHH')"><li>HOME</li></a>
                        <a onclick="showPage('idHA')"><li>AVISOS</li></a>
                        <a><li class="homeSelect">FACULRIDES</li></a>
                        <a onclick="showPage('idHE')"><li>ESTÁGIOS</li></a>
                    </ul>
                </nav>
            </div>
            
            <div class="divForm">
                <form class="formFaculRides pagina" action="" id="frForm">
                    <h1 class="titleForm">PARA PARTICIPAR, PREENCHA O FORMULÁRIO!</h1>
                    <div class="info_endereco">

                        <div class="labels_endereco">
                            <label for="frRua">Rua:</label>
                            <label for="frNum">Número:</label>
                            <label for="frComp">Complemento:</label>
                            <label for="frRef">Referência:</label>
                            <label for="frTel">Telefone:</label>
                        </div>

                        <div class="inputs_endereco">
                            <input type="text" name="frRua" id="idfrRua" required>
                            <input type="text" name="frNum" id="idfrNum" required>
                            <input type="text" name="frComp" id="idfrComp" placeholder="(Opcional)">
                            <input type="text" name="frRef" id="idfrRef" placeholder="(Opcional)">
                            <input type="text" name="frTel" id="idfrTel" required>
                        </div>
                        
                    </div>

                    <div class="checkbox_termos">
                        <input type="checkbox" name="frConc" id="idfrConc" required>
                        <label class="label" for="frConc">Declaro que estou de acordo com a utilização do meu endereço para localizar estudantes da minha região.</label>
                    </div>
                    
                    <div class="submitForm">
                        <input type="submit" value="Vamos lá!" onclick="tirablur('blurFR')">
                    </div>
                </form>
            </div>

            <div class="partFR blur" id="blurFR">
                <p style="text-align: center;">*CLIQUE NO PERFIL PARA SABER MAIS*</p>
                <div class="pessoaBox" onclick="revealTxt('pessoaXXX')">
                    <div class="infoPessoa">
                        <img src="../images/perfil.png" width="40px" height="40px">
                        <h4>Pessoa X</h4>
                        <h4>Água Verde</h4>
                    </div>
                    <p class="textPessoa" id="pessoaXXX">Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis, officia soluta voluptatem, iure reprehenderit ut consequatur nostrum accusamus, explicabo quaerat doloremque animi modi atque enim vitae in ullam. Nisi, tenetur! Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ducimus adipisci alias quasi incidunt culpa! Ipsa repellat modi ex eos quam consequuntur esse, magni vero nulla cum incidunt quas dicta earum.</p>
                </div>
                
                <div class="pessoaBox" onclick="revealTxt('pessoaYYY')">
                    <div class="infoPessoa">
                        <img src="../images/perfil.png" width="40px" height="40px">
                        <h4>Pessoa Y</h4>
                        <h4>Centro</h4>
                    </div>
            
                    <p class="textPessoa" id="pessoaYYY">Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis, officia soluta voluptatem, iure reprehenderit ut consequatur nostrum accusamus, explicabo quaerat doloremque animi modi atque enim vitae in ullam. Nisi, tenetur! Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ducimus adipisci alias quasi incidunt culpa! Ipsa repellat modi ex eos quam consequuntur esse, magni vero nulla cum incidunt quas dicta earum.</p>
                </div>

                <div class="pessoaBox" onclick="revealTxt('pessoaZZZ')">
                    <div class="infoPessoa">
                        <img src="../images/perfil.png" width="40px" height="40px">
                        <h4>Pessoa Z</h4>
                        <h4>Seminário</h4>
                    </div>
                    
                    <p class="textPessoa" id="pessoaZZZ">Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis, officia soluta voluptatem, iure reprehenderit ut consequatur nostrum accusamus, explicabo quaerat doloremque animi modi atque enim vitae in ullam. Nisi, tenetur! Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ducimus adipisci alias quasi incidunt culpa! Ipsa repellat modi ex eos quam consequuntur esse, magni vero nulla cum incidunt quas dicta earum.</p>
                </div>
            </div>
        </div>


        <!-- ESTÁGIO -->

        <div class="containerH subpagina" id="idHE">
            <div class="navHome">
                <nav>
                    <ul>
                        <a onclick="showPage('idHH')"><li>HOME</li></a>
                        <a onclick="showPage('idHA')"><li>AVISOS</li></a>
                        <a onclick="showPage('idHF')"><li>FACULRIDES</li></a>
                        <a><li class="homeSelect">ESTÁGIOS</li></a>
                    </ul>
                </nav>
            </div>

                <div class="estTitle">
                    <h3>Logo</h3>
                    <h3>Empresa</h3>
                    <h3>Área</h3>
                    <h3>Detalhes</h3>
                    
                </div>

                <div style="margin: auto;">
                    <div class="estBox" onclick="revealTxt('estagioXXX')">
                        <div class="infoEstagio">
                            <img src="../images/empresa.png" alt="Empresa X">
                            <p>Empresa X</p>
                            <p>Análise de Sitstemas</p>
                            <h3>VER</h3>
                        </div>
                        <p class="textEstagio" id="estagioXXX">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Odit sunt dolorum sed? Quos aliquam qui totam unde iure. Quae ab mollitia aliquam earum in iste totam similique accusantium quam eligendi. Lorem ipsum dolor sit amet consectetur adipisicing elit. At quisquam vel, deserunt labore omnis corporis reprehenderit, quam, sed provident eveniet assumenda mollitia id consectetur placeat. Consequuntur facere architecto minus in. Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem sapiente vel a assumenda praesentium quia harum nam rerum amet libero ducimus in architecto, aut dolorum atque ab facilis nisi quod?</p>
                    </div>

                    <div class="estBox" onclick="revealTxt('estagioYYY')">
                        <div class="infoEstagio">
                            <img src="../images/empresa.png" alt="Empresa Y">
                            <p>Empresa Y</p>
                            <p>Desenvolvimento Python</p>
                            <h3>VER</h3>
                        </div>
                        <p class="textEstagio" id="estagioYYY">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Odit sunt dolorum sed? Quos aliquam qui totam unde iure. Quae ab mollitia aliquam earum in iste totam similique accusantium quam eligendi. Lorem ipsum dolor sit amet consectetur adipisicing elit. At quisquam vel, deserunt labore omnis corporis reprehenderit, quam, sed provident eveniet assumenda mollitia id consectetur placeat. Consequuntur facere architecto minus in. Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem sapiente vel a assumenda praesentium quia harum nam rerum amet libero ducimus in architecto, aut dolorum atque ab facilis nisi quod?</p>
                    </div>

                    <div class="estBox" onclick="revealTxt('estagioZZZ')">
                        <div class="infoEstagio">
                            <img src="../images/empresa.png" alt="Empresa Z">
                            <p>Empresa Z</p>
                            <p>Gestão de Projetos</p>
                            <h3>VER</h3>
                        </div>
                        <p class="textEstagio" id="estagioZZZ">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Odit sunt dolorum sed? Quos aliquam qui totam unde iure. Quae ab mollitia aliquam earum in iste totam similique accusantium quam eligendi. Lorem ipsum dolor sit amet consectetur adipisicing elit. At quisquam vel, deserunt labore omnis corporis reprehenderit, quam, sed provident eveniet assumenda mollitia id consectetur placeat. Consequuntur facere architecto minus in. Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem sapiente vel a assumenda praesentium quia harum nam rerum amet libero ducimus in architecto, aut dolorum atque ab facilis nisi quod?</p>
                    </div>
                </div>  

                    


        </div>

        

    </main>

    <footer >
        <p>Todos os direitos reservados - Ícaro Kuchanovicz - Ary Farah - Adriano Vale - Caroline Assis</p>
    </footer>
</body>
</html>