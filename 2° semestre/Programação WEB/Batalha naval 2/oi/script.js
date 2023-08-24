function tabela() {
    for(i=0; i<5; i++) {
        document.write("<tr>")
        for(j=0; j<8; j++) {
            document.write(`<td width=50 onclick='shipOnClick(${i}, ${j})'><img id='ship${i}${j}' width=50 src='images/back.jpg'></td>`)
        }
        document.write("</tr>")
    }
}


const ships = [
    [0, 1, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 3, 0, 0, 0],
    [1, 0, 2, 0, 0, 0, 1, 0]];
let life;
let points;
let endGame;

function resetGame() {

life = 5;
points = 0;
endGame = false;
shuffle();
}



function shuffle() {

for(i=0; i<1000; i++) {
    i1 = Math.floor(Math.random() * 5);
    j1 = Math.floor(Math.random() * 8);
    i2 = Math.floor(Math.random() * 5);
    j2 = Math.floor(Math.random() * 8);
    let temp = ships[i1][j1];
    ships[i1][j1] = ships[i2][j2];
    ships[i2][j2] = temp;
}
}



function shipOnClick(indX, indY) {

if (endGame) return;

const ship = document.getElementById(`ship${indX}${indY}`);
const type = ships[indX][indY];
ship.src = getImage(type);
update_scoreboard(type);
}





function getImage(type) {
switch (type) {
    case 0:
        return "images/agua.jpg";
        break;
    case 1:
        return "images/submarino.jpg";
        break;
    case 2:
        return "images/porta_avioes.jpg";
        break;
    case 3:
        return "images/navio_de_guerra.jpg";
        break;
}

return "images/back.jpg";
}

function update_scoreboard(type) {

points += type;
if (type == 0) {
    life--;
    update_scoreboard_view();
    if (life == 0) {
        alert('Jogo Concluído!!!');
        endGame = true;
    }
}
else {
    update_scoreboard_view();
}
}

function update_scoreboard_view() {

const scoreboard = document.getElementById("divScoreboard");
scoreboard.innerHTML = "Pontos: " + points + " - Vidas: " + life;
}

tabela();
resetGame();