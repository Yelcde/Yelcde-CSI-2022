package conta;

public class Conta {
    private String numero;
    private String cpf;
    private double saldo;
    
    public Conta(String numero, String cpf) {
        this.numero = numero;
        this.cpf = cpf;
        this.saldo = 0;
    }

    // Funções
    public double getSaldo() {
        return saldo;
    }

    public void creditar(double valor) {
        saldo = (saldo + valor);
    }

    public void debitar(double valor) {
        saldo = (saldo - valor);
    }
}
