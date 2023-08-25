package aluno;

public class Main {
    public static void main(String[] args) {
        Aluno aluno = new Aluno("Johnner", 40, 40);
        System.out.println("O aluno " + aluno.getNome() + " com a média " + aluno.getMedia() + " está " + aluno.getSituacao());
    }
}
