var barcos = [];
var vidas;
var pontos;
var pode;
var count = 0;
var vidamax = 5;

function aleat(min, max){

    var aleat = Math.floor(Math.random() * (max - min + 1)) + min;
    return aleat
}





function newgame(){
for (var i = 0; i < 16; i++) {
    barcos.push(0);
}

sorteados = []

do {
    var pos = aleat(0, 15);
    if (sorteados.includes(pos)){
        continue;
    } else{
        barcos[pos] = 1;
        sorteados.push(pos);
    }
} while (sorteados.length < 3)


vidas = vidamax;
pontos = 0
pode = true;





alert(barcos)

}



function clicar(id){
    var peça = window.document.getElementById(id);

//    alert('ID: '+ id)
    if(pode == true){
        verifStatus(id)
    }

    // peça.style.backgroundImage = 'url(images/water.png)';
    // peça.style.backgroundSize = 'cover';

    // alert('Elemento clicado: '+ id);

}


function verifStatus(x){
 //   alert(x)
    var peça = window.document.getElementById(x)
    var pontoht = window.document.getElementById('pontos')
    var vidaht = window.document.getElementById('vidas')

    if (barcos[x-1] == 0){
        peça.style.backgroundImage = 'url(images/water.png)';
        peça.style.backgroundSize = 'cover';

        vidas -= 1;
        vidaht.innerText = vidas

        if (vidas <= 0){
            gameover();
        }

        if(pontos>0){
            pontos -= 1;
            pontoht.innerText = pontos
        }






    } else {
        count += 1
        peça.style.backgroundImage = 'url(images/ship.png)';
        peça.style.backgroundSize = 'cover';

        if (vidas < vidamax){
            vidas += 1;
            vidaht.innerText = vidas
        }
        pontos += 1
        pontoht.innerText = pontos
        if(count == 3){
            win()
        }

    }
}


function gameover(){
    pode = false;
    alert('VOCE PERDEU\nPontos: '+ pontos)

}


function win(){
    pode = false;
    alert('VOCE GANHOU!!!\nPontos: '+ pontos)
}