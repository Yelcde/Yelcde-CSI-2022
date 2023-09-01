package contaEx;

public class Conta {
    private String numero;
    private String cpf;
    private Integer saldo;
    
    public Conta(String numero, String cpf) {
        this.numero = numero;
        this.cpf = cpf;
        this.saldo = 0;
    }

    // Funções
    public Integer getSaldo() {
        return saldo;
    }

    public void creditar(Integer valor) {
        saldo = saldo + valor;
    }

    public void debitar(Integer valor) {
        saldo = saldo - valor;
    }

    public boolean vazia() {
        if (this.saldo == 0) {
            return true;
        } else {
            return false;
        }
    }

    public Conta clonar() {
        return new Conta(this.numero, this.cpf);
    }

    public String toString() {
        return  " numero = " + numero +
                " cpf = " + cpf +
                " saldo = " + saldo;
    }
}
