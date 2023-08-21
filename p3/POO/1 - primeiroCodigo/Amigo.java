import java.util.Scanner;

public class Amigo {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.println("Qual é o seu nome? ");
        String nome1 = teclado.nextLine();
        System.out.println(nome1+", de quem você é amigo? ");
        String nome2 = teclado.nextLine();
        System.out.println(nome1+" é amigo de "+nome2);
        teclado.close();
    }
}