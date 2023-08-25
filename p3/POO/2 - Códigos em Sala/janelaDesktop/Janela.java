import javax.swing.JFrame;

public class Janela {
    public static void main(String[] args) {
        JFrame janela = new JFrame();
        janela.setTitle("Exemplo de Janela");
        janela.setSize(500,300); //width, height
        janela.setResizable(false);
        janela.setVisible(true);
    }
}
