public class Vagas {
    public static void main(String[] args){
        try{

            Estacionamento e = new Estacionamento(10); // 10 vagas
            e.entrar("AAA1000",1); // ocupa a vaga 1
            e.entrar("XXX7000",2); // ocupa a vaga 2
            e.entrar("PPP4000",5); // ocupa a vaga 5
            System.out.println(e.entrar("BBB5000")); // ocupa a vaga 3 e retorna 3
            System.out.println(e.entrar("TTT9000")); // ocupa a vaga 4 e retorna 4
            System.out.println(e.listarLivres()); // exibe [6,7,8,9,10]
        }
        catch (Exception ex){
            System.out.println(ex.getMessage());
        }
    }
}
