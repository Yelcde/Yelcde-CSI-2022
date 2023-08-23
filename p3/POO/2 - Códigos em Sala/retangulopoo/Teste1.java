package retangulopoo;

public class Teste1 {
    public static void main(String[] args){
        Retangulo r1 = new Retangulo(1, 3, 4);
        System.out.println(r1.calcularArea());

        Retangulo r2 = new Retangulo();
        System.out.println(r2.calcularArea());

        Retangulo r3 = new Retangulo(1, 3, 5);
        System.out.println(r3.calcularArea() + " r3 Sem enquadrar");
        System.out.print("r3 enquadrado ");
        r3.enquadrar();
        System.out.println(r3.largura + " " + r3.comprimento);
    }
}
