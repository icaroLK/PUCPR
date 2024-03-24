public class Main {
    public static void main(String[] args){

        Netflix filme = new Netflix();
        filme.nome = "Vingadores";
        filme.duracao = 3.02f;
        filme.genero = "Ação/Ficção";
        filme.classificacao = 12;
        filme.pausado = true;
        filme.diretor = "Castro Brothers";
        filme.tipo = 'F';
        filme.legenda = false;
        filme.idioma = "Ingles";
        filme.tempoDecorrido = 0;
        filme.anoLancamento = 2019;

        System.out.println("\nO filme " + filme.nome + " criado pelos " + filme.diretor + " tem duração de " + filme.duracao + " horas\n");



        System.out.println(filme.nome);
        System.out.println(filme.duracao);
        System.out.println(filme.genero);
        System.out.println("Classificação: +" + filme.classificacao);
        System.out.println("Pausado? " + filme.pausado);
        System.out.println(filme.diretor);
        System.out.println(filme.tipo);
        System.out.println("Legenda ligada? " + filme.legenda);
        System.out.println(filme.idioma);
        System.out.println("Tempo decorrido: " + filme.tempoDecorrido);
        System.out.println(filme.anoLancamento);

    }
}