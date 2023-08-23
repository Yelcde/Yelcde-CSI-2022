package retangulopoo;

public class Retangulo {
    public int id;
    public double largura;
    public double comprimento;

    //  Construtor
    public Retangulo(int id, double largura, double comprimento){
        this.id = id;
        this.largura = largura;
        this.comprimento = comprimento;
    }

    public Retangulo() { }

    public double calcularArea() {
        return largura * comprimento;
    }

    public void enquadrar() {
        double media = (largura+comprimento) / 2;
        largura = media;
        comprimento = media;
    }
}
