import java.util.ArrayList;

import javax.swing.JOptionPane;

public class Gabarito {
    public static void main(String[] args) {
        ArrayList<String> gabarito = new ArrayList<>();
        gabarito.add("a");
        gabarito.add("a");
        gabarito.add("e");
        gabarito.add("e");
        gabarito.add("c");
        gabarito.add("b");
        gabarito.add("d");
        gabarito.add("b");
        gabarito.add("c");
        gabarito.add("d");

        ArrayList<String> respostaAluno = new ArrayList<>();

        int nota = 0;

        for (int i = 0; i < gabarito.size(); i++){
            String teclado = JOptionPane.showInputDialog(null, "Qual a sua resposta para o item " + (i+1) + " da prova");
            respostaAluno.add(teclado);
            if (gabarito.get(i).equals(respostaAluno.get(i))){
                nota++;
            }
        }

        JOptionPane.showMessageDialog(null, "Sua nota é " + nota);
    }
}
