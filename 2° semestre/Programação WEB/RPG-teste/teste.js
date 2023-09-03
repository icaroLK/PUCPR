


const cores = {
    cinza: '#4b4b4b',
    azul: 'rgb(145, 133, 238)',


}

const up = document.getElementById('up');
const right = document.getElementById('right');
const left = document.getElementById('left');
const down = document.getElementById('down');
const bola = document.getElementById('bola');



function iniciarJogo(){

    const iniciar = document.querySelector('.iniciar');
    const textoini = document.querySelector('.textoini');

    const textarea = document.querySelector('.textarea');
    const joystick = document.querySelector('.joystick');
    const map = document.querySelector('.map');
    const body = document.querySelector('body');


    joystick.style.opacity = "1";
    textarea.style.opacity = "1";
    textoini.classList.add("fadeOut");
    iniciar.classList.add("fadeOut");
    
    map.style.height = '40vh';
    map.style.width = '80vh';
    map.style.transition = 'ease-in-out 6s';

    // body.style.backgroundImage = 'linear-gradient(45deg, #111855, #25451b)';
    

}







function joystick(opa){
var botao = document.getElementById(opa)
window.alert("voce apertou   " + opa)
}




document.addEventListener("keydown", function(event) {
    if (event.key === "ArrowUp") {
        up.style.borderTop = `5px solid ${cores.azul}`;
        up.style.borderRight = `5px solid ${cores.azul}`;
        up.style.borderLeft = `5px solid ${cores.azul}`;

    } else if (event.key === "ArrowDown") {
        down.style.borderRight = `5px solid ${cores.azul}`;
        down.style.borderBottom = `5px solid ${cores.azul}`;
        down.style.borderLeft = `5px solid ${cores.azul}`;

    } else if (event.key === "ArrowLeft") {
        left.style.borderTop = `5px solid ${cores.azul}`;
        left.style.borderBottom = `5px solid ${cores.azul}`;
        left.style.borderLeft = `5px solid ${cores.azul}`;

    } else if (event.key === "ArrowRight") {
        right.style.borderTop = `5px solid ${cores.azul}`;
        right.style.borderBottom = `5px solid ${cores.azul}`;
        right.style.borderRight = `5px solid ${cores.azul}`;
        
    } else if (event.key === "Enter") {
        bola.style.border = `3px solid ${cores.azul}`;
    }
});

document.addEventListener("keyup", function(event) {
    if (event.key === "ArrowUp") {
        up.style.borderTop = `5px solid ${cores.cinza}`;
        up.style.borderRight = `5px solid ${cores.cinza}`;
        up.style.borderLeft = `5px solid ${cores.cinza}`;

    } else if (event.key === "ArrowDown") {
        down.style.borderRight = `5px solid ${cores.cinza}`;
        down.style.borderBottom = `5px solid ${cores.cinza}`;
        down.style.borderLeft = `5px solid ${cores.cinza}`;

    } else if (event.key === "ArrowLeft") {
        left.style.borderTop = `5px solid ${cores.cinza}`;
        left.style.borderBottom = `5px solid ${cores.cinza}`;
        left.style.borderLeft = `5px solid ${cores.cinza}`;

    } else if (event.key === "ArrowRight") {
        right.style.borderTop = `5px solid ${cores.cinza}`;
        right.style.borderBottom = `5px solid ${cores.cinza}`;
        right.style.borderRight = `5px solid ${cores.cinza}`;

    } else if (event.key === "Enter") {
        bola.style.border = `5px solid ${cores.cinza}`;
    }
});


