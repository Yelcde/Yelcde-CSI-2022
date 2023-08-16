import javax.swing.JOptionPane;

public class Amigo2 {
    public static void main(String[] args) {
        String nome1 = JOptionPane.showInputDialog("Qual é o seu nome?");
        String nome2 = JOptionPane.showInputDialog(nome1 + " quem é o seu amigo?");
        JOptionPane.showMessageDialog(null, nome1 + " é amigo de " + nome2);
    }
}