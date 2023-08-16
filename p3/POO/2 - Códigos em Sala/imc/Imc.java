public class Imc {
    public static void main(String[] args){
        double peso = 150;
        double altura = 1.70;
        double imc = peso / Math.pow(altura, 2);
        if (imc < 18.5)
            System.out.println("Abaixo do normal");
        else
            if (imc < 24.9)
                System.out.println("Normal");
            else
                if (imc < 29.9)
                    System.out.println("Sobrepeso");
                else
                    if (imc < 34.9)
                        System.out.println("Obesidade grau I");
                    else 
                        if (imc < 39.9)
                            System.out.println("Obesidade grau II");
                        else
                            if (imc > 39.9)
                                System.out.println("Obesidade grau III");
    } 
}
