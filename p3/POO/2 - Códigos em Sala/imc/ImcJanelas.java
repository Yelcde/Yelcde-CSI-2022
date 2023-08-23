package imc;

import javax.swing.JOptionPane;

public class ImcJanelas {
    public static void main(String[] args){
        try{
            // ler peso e altura como string e converter
            double peso = Double.parseDouble(JOptionPane.showInputDialog(null, "Qual é o seu peso?"));
            double altura = Double.parseDouble(JOptionPane.showInputDialog(null, "Qual é a sua altura?"));
            double imc = peso / Math.pow(altura, 2);
            if (imc < 18.5)
                JOptionPane.showMessageDialog(null, "Abaixo do normal");
            else
                if (imc < 24.9)
                    JOptionPane.showMessageDialog(null, "Normal");
                else
                    if (imc < 29.9)
                        JOptionPane.showMessageDialog(null, "Sobrepeso");
                    else
                        if (imc < 34.9)
                            JOptionPane.showMessageDialog(null, "Obesidade grau I");
                        else 
                            if (imc < 39.9)
                                JOptionPane.showMessageDialog(null, "Obesidade grau II");
                            else
                                if (imc > 39.9)
                                    JOptionPane.showMessageDialog(null, "Obesidade grau III");
            }
            catch(Exception e){
                JOptionPane.showMessageDialog(null, "formato do numero incorreto");
                System.exit(0); //termina programa
            }
    } 
}