package aluno;

public class Aluno {
    // Criação dos atributos
    private String nome;
    private Integer nota1;
    private Integer nota2;

    public Aluno(String texto, int nota1, int nota2) {
        this.nome = texto;
        this.nota1 = nota1;
        this.nota2 = nota2;
    }    
    
    // Metodos get
    public String getNome() {
        return nome;
    }

    public Integer getMedia() {
        return (nota1 + nota2) / 2;
    }

    public String getSituacao() {
        if (this.getMedia() >= 70)
            return "Aprovado";
        else if (this.getMedia() >= 40)
            return "Reprovado";
        else return "Final";
    }
}
