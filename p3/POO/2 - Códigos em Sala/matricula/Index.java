public class Index {
    public static void main(String[] args) {
        Matricula matricula = new Matricula("20222370015");
        System.out.println("Ano: " + matricula.getAno());
        System.out.println("Periodo: " + matricula.getPeriodo());
        System.out.println("Código do Curso: " + matricula.getCodigoCurso());
        System.out.println("Sequencia: " + matricula.getSequencia());
    }
}
