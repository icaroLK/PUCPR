// HOME
function showPage(id) {

  const subpag = document.querySelectorAll('.subpagina');
  subpag.forEach(sp => {
      sp.classList.remove('pagina');
  });

  const selectSubpag = document.getElementById(id);
  selectSubpag.classList.add('pagina');

}

function some(id) {
  
  const pagagr = document.getElementById(id);
  pagagr.classList.add('subpagina')

}

// AVISOS
function revealTxt(id) {

    var txt = document.getElementById(id)
    
    if (txt.style.display === 'none') {
        txt.style.display = 'block'; // Mostra o conteúdo ao clicar

    } else {
        txt.style.display = 'none'; // Oculta o conteúdo se já estiver visível
    }

}

function selectSem() {
  var select = document.getElementById('idselSem')
  var selectedPage = select.value;

  var subpag = document.getElementsByClassName('subpagina')
  for (var i = 0; i < subpag.length; i++) {
    subpag[i].style.display = 'none'
  }

  document.getElementById(selectedPage).classList.remove('subpagina')
}


// FACULRIDES
function tirablur(id, pag) {
  const blur = document.getElementById(id)
  blur.classList.remove('blur')
}




// ESTÁGIO






// NOTAS
let materiasEscolhidas = [];

function selecionarMaterias() {
  const cursos = {
    direito: ['Direito Civil', 'Direito Criminal', 'Ética', 'Direito Constitucional', 'Direito Administrativo', 'Direito do Trabalho'],
    medicina: ['Anatomia', 'Fisiologia', 'Bioquímica', 'Patologia', 'Farmacologia', 'Clínica Médica'],
    engenharia: ['Cálculo', 'Física', 'Química', 'Algoritmos', 'Estruturas de Dados', 'Engenharia de Software']
  };

  const cursoEscolhido = Object.keys(cursos)[Math.floor(Math.random() * 3)];
  materiasEscolhidas = cursos[cursoEscolhido];

  localStorage.setItem('materiasEscolhidas', JSON.stringify(materiasEscolhidas));
}

document.addEventListener('DOMContentLoaded', function() {
  selecionarMaterias();
});

function preencherTabelaNotas() {
    const tabela = document.getElementById('tabela-notas');
    if (!tabela) return;
  
    const materiasEscolhidas = JSON.parse(localStorage.getItem('materiasEscolhidas')) || [];
  
    const cabecalho = tabela.createTHead().insertRow();
    cabecalho.insertCell().textContent = 'Matérias';
    cabecalho.insertCell().textContent = 'Notas';
    cabecalho.insertCell().textContent = 'Frequência';
  
    const corpoTabela = tabela.createTBody();
    for (let i = 0; i < 6; i++) {
      const linha = corpoTabela.insertRow();
      linha.insertCell().textContent = materiasEscolhidas[i];
      linha.insertCell().textContent = (Math.random() * 4 + 6).toFixed(2);
      linha.insertCell().textContent = Math.floor(Math.random() * 31 + 70) + '%';
    }
  }
  
  document.addEventListener('DOMContentLoaded', function() {
    preencherTabelaNotas();
  });




//ATIVIDADES COMPLEMENTARES





// AULAS
function preencherTabelaAulas() {
    const tabela = document.getElementById('tabela-aulas');
    if (!tabela) return;
  
    const materiasEscolhidas = JSON.parse(localStorage.getItem('materiasEscolhidas')) || [];
  
    const cabecalho = tabela.createTHead().insertRow();
    cabecalho.insertCell().textContent = 'Matérias';
    cabecalho.insertCell().textContent = 'Carga Horária';
  
    const corpoTabela = tabela.createTBody();
    for (const materia of materiasEscolhidas) {
      const linha = corpoTabela.insertRow();
      linha.insertCell().textContent = materia;
      linha.insertCell().textContent = Math.random() > 0.5 ? '120 horas' : '80 horas';
    }
  }
  
  document.addEventListener('DOMContentLoaded', function() {
    preencherTabelaAulas();
  });
  

// POSIÇÃO FINANCEIRA