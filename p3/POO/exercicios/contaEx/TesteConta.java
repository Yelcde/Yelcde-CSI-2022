package contaEx;

public class TesteConta {
    public static void main(String[] args) {
        Conta conta1 = new Conta("123", "12345");
        conta1.creditar(300);
        //conta1.debitar(300);
        //System.out.println(conta1.vazia());

        Conta conta2 = conta1.clonar();
        System.out.println(conta1); //333,123456,300
        System.out.println(conta2);
    }
}