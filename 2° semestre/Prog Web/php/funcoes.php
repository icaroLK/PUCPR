<?php


$banco = new mysqli("127.0.0.1", "root", "PUC@1234", "Universe");


session_start();


if(!(isset($_SESSION['usuario']))){
    $_SESSION['usuario'] = '';
    $_SESSION['nome'] = '';
    $_SESSION['email'] = '';
    $_SESSION['tipo'] = '';
}








function msg_erro($msg){
return "<div class='msg erro'><span class='material-symbols-outlined'>error</span>$msg</div>";
};


function msg_aviso($msg){
    return "<div class='msg erro'><span class='material-symbols-outlined'>warning</span>$msg</div>";
};
    
    
function msg_sucesso($msg){
    return "<div class='msg erro'><span class='material-symbols-outlined'>check</span>$msg</div>";
};
        
        
    

function logout(){
    unset($_SESSION['usuario']);
    unset($_SESSION['nome']);
    unset($_SESSION['email']);
    unset($_SESSION['tipo']);
}
