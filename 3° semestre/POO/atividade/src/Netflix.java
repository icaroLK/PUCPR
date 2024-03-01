public class Netflix {
    public String nome;
    public float duracao;
    public String genero;
    public int classificacao;
    public boolean pausado;
    public String diretor;
    public char tipo;
    public boolean legenda;
    public String idioma;
    public float tempoDecorrido;
    public int anoLancamento;


    public void play(){
        if (this.pausado == true){
            this.pausado = false;
        }else{
            this.pausado = true;
        }
    }

    public void pular(int x){
        this.tempoDecorrido += x;
    }

    public void ligarLegenda(){
        if (this.legenda == true){
            this.legenda = false;
        }else{
            this.legenda = true;
        }
    }


}
