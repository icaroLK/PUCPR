//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Filme Filme1 = new Filme();

        System.out.println("----------------FILME-------------------\n");
        System.out.println("Nome do filme 1: " + Filme1.getNome());
        System.out.println("Gênero do filme 1: "+ Filme1.getGenero());
        System.out.println("Classificação do filme 1: +"+ Filme1.getClassificacao());
        System.out.println("Diretor do filme 1: "+ Filme1.getDiretor());
        System.out.println("----------------------------------------------\n");


        Filme Filme2 = new Filme(2.3f, "Vingadores", "Castro Brothers", "Ação", 12);

        System.out.println("----------------FILME-------------------\n");
        System.out.println("Nome do filme 2: " + Filme2.getNome());
        System.out.println("Gênero do filme 2: "+ Filme2.getGenero());
        System.out.println("Classificação do filme 2: +"+ Filme2.getClassificacao());
        System.out.println("Diretor do filme 2: "+ Filme2.getDiretor());
        System.out.println("----------------------------------------------\n");


        Serie Serie1 = new Serie();
        System.out.println("----------------SERIE-------------------\n");
        System.out.println("Nome da série 1: " + Serie1.getNome());
        System.out.println("Gênero da série 1: "+ Serie1.getGenero());
        System.out.println("Classificação da série 1: +"+ Serie1.getClassificacao());
        System.out.println("Quantidade de episódios da série 1: "+ Serie1.getEpisodios());
        System.out.println("----------------------------------------------\n");


        Serie Serie2 = new Serie(0.45f, "Lucifer", 12, "Romance", 16);
        System.out.println("----------------SERIE-------------------\n");
        System.out.println("Nome da série 2: " + Serie2.getNome());
        System.out.println("Gênero da série 2: "+ Serie2.getGenero());
        System.out.println("Classificação da série 2: +"+ Serie2.getClassificacao());
        System.out.println("Quantidade de episódios da série 2: "+ Serie2.getEpisodios());
        System.out.println("----------------------------------------------\n");




        Miniserie Miniserie1 = new Miniserie();
        System.out.println("----------------MINISERIE-------------------\n");
        System.out.println("Nome da miniserie 1: " + Miniserie1.getNome());
        System.out.println("Gênero da miniserie 1: "+ Miniserie1.getGenero());
        System.out.println("Classificação da miniserie 1: +"+ Miniserie1.getClassificacao());
        System.out.println("Quantidade de episódios da miniserie 1: "+ Miniserie1.getEpisodios());
        System.out.println("----------------------------------------------\n");


        Miniserie Miniserie2 = new Miniserie(30.0f, "Formula 1", 3, "Documentário", 12);
        System.out.println("----------------MINISERIE-------------------\n");
        System.out.println("Nome da miniserie 2: " + Miniserie2.getNome());
        System.out.println("Gênero da miniserie 2: "+ Miniserie2.getGenero());
        System.out.println("Classificação da miniserie 2: +"+ Miniserie2.getClassificacao());
        System.out.println("Quantidade de episódios da miniserie 2: "+ Miniserie2.getEpisodios());
        System.out.println("----------------------------------------------\n");

    }
}