package conta;

public class ContaTeste {
    public static void main(String[] args) {
        Conta conta1 = new Conta("101", "123456");
        conta1.creditar(300);
        System.out.println(conta1.getSaldo());
        conta1.debitar(100);
        System.out.println(conta1.getSaldo());
        conta1.creditar(200);
    }
}
