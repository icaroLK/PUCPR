const cores = {
    cinza: '#4b4b4b',
    azul: 'rgb(145, 133, 238)',
}

const up = document.getElementById('up');
const right = document.getElementById('right');
const left = document.getElementById('left');
const down = document.getElementById('down');
const bola = document.getElementById('bola');



var level = 0

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
    map.style.transition = 'ease-in-out 3s';

    // body.style.backgroundImage = 'linear-gradient(45deg, #111855, #25451b)';
    

}







function joystick(opa){
var botao = document.getElementById(opa)
// window.alert("voce apertou   " + opa)

if(opa == 'bola'){
    quest(level)
}

}




document.addEventListener("keydown", function(event) {
    if (event.key === "ArrowUp") {
        up.style.borderTop = `5px solid ${cores.azul}`;
        up.style.borderRight = `5px solid ${cores.azul}`;
        up.style.borderLeft = `5px solid ${cores.azul}`;
        joystick('up')

    } else if (event.key === "ArrowDown") {
        down.style.borderRight = `5px solid ${cores.azul}`;
        down.style.borderBottom = `5px solid ${cores.azul}`;
        down.style.borderLeft = `5px solid ${cores.azul}`;
        joystick('down')

    } else if (event.key === "ArrowLeft") {
        left.style.borderTop = `5px solid ${cores.azul}`;
        left.style.borderBottom = `5px solid ${cores.azul}`;
        left.style.borderLeft = `5px solid ${cores.azul}`;
        joystick('left')

    } else if (event.key === "ArrowRight") {
        right.style.borderTop = `5px solid ${cores.azul}`;
        right.style.borderBottom = `5px solid ${cores.azul}`;
        right.style.borderRight = `5px solid ${cores.azul}`;
        joystick('right')
        
    } else if (event.key === "Enter") {
        bola.style.border = `3px solid ${cores.azul}`;
        joystick('bola')
    }
});

document.addEventListener("keyup", function(event) {
    if (event.key === "ArrowUp") {
        up.style.borderTop = `5px solid ${cores.cinza}`;
        up.style.borderRight = `5px solid ${cores.cinza}`;
        up.style.borderLeft = `5px solid ${cores.cinza}`;
        joystick('up')

    } else if (event.key === "ArrowDown") {
        down.style.borderRight = `5px solid ${cores.cinza}`;
        down.style.borderBottom = `5px solid ${cores.cinza}`;
        down.style.borderLeft = `5px solid ${cores.cinza}`;
        joystick('down')

    } else if (event.key === "ArrowLeft") {
        left.style.borderTop = `5px solid ${cores.cinza}`;
        left.style.borderBottom = `5px solid ${cores.cinza}`;
        left.style.borderLeft = `5px solid ${cores.cinza}`;
        joystick('left')

    } else if (event.key === "ArrowRight") {
        right.style.borderTop = `5px solid ${cores.cinza}`;
        right.style.borderBottom = `5px solid ${cores.cinza}`;
        right.style.borderRight = `5px solid ${cores.cinza}`;
        joystick('right')

    } else if (event.key === "Enter") {
        bola.style.border = `5px solid ${cores.cinza}`;
        joystick('bola')
    }
});




const mainText = document.querySelector('.mainText');

function quest(xota){
    // window.alert('cu')
    if(xota == 0){
        mainText.innerHTML = 'Era uma vez uma garotinha chamada Kenny';
        level = 2;
    }
    else if (xota == 1){
        mainText.innerHTML = 'que vivia uma vida normal com sua vó, em uma pequena casa de madeira';
        level = 4;
    }


}