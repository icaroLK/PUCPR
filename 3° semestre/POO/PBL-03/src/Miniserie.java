public class Miniserie {

    private float duracao;
    private String nome;
    private int episodios;
    private String genero;
    private int classificacao;

    public Miniserie() {
        this.duracao = 0;
        this.nome = "Desconhecido";
        this.episodios = 0;
        this.genero = "Não tem";
        this.classificacao = 0;
    }


    public Miniserie(float duracao, String nome, int episodios, String genero, int classificacao){

        this.duracao = duracao;
        this.nome = nome;
        this.episodios = episodios;
        this.genero = genero;
        this.classificacao = classificacao;
    }


    public float getDuracao(){
        return this.duracao;
    }
    public void setDuracao(float duracao){
        this.duracao = duracao;
    }



    public String getNome(){
        return this.nome;
    }
    public void setNome(String nome){
        this.nome = nome;
    }


    public String getGenero(){
        return this.genero;
    }
    public void setGenero(String genero){
        this.genero = genero;
    }


    public int getEpisodios(){
        return this.episodios;
    }
    public void setEpisodios(int episodios){
        this.episodios = episodios;
    }



    public int getClassificacao(){
        return this.classificacao;
    }
    public void setClassificacao(int classificacao){
        this.classificacao = classificacao;
    }

}

