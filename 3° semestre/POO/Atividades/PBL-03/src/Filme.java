public class Filme {

    private float duracao;
    private String nome;
    private String diretor;
    private String genero;
    private int classificacao;

    public Filme() {
        this.duracao = 0;
        this.nome = "Desconhecido";
        this.diretor = "Ninguém";
        this.genero = "Não tem";
        this.classificacao = 0;
    }


    public Filme(float duracao, String nome, String diretor, String genero, int classificacao){

        this.duracao = duracao;
        this.nome = nome;
        this.diretor = diretor;
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


    public String getDiretor(){
        return this.diretor;
    }
    public void setDiretor(String diretor){
        this.diretor = diretor;
    }



    public int getClassificacao(){
        return this.classificacao;
    }
    public void setClassificacao(int classificacao){
        this.classificacao = classificacao;
    }

}

