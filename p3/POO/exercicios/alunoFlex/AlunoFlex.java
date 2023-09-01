package alunoFlex;

import java.lang.reflect.Array;
import java.util.ArrayList;

public class AlunoFlex {
    private String nome;
    private ArrayList<Double> notas = new ArrayList<Double>();

    public AlunoFlex(String nome, double... notas) {
        this.nome = nome;

        for (double nota: notas) {
            this.notas.add(nota);
        }
    }

    public String getNome(){
        return this.nome;
    }

    public double getMedia() {
        double soma = 0;
        double i = 0;
        for (double nota: notas){
            soma = soma + nota;
            i = i + 1;
        }
        return soma / i;
    }

    public String getSituacao() {
        if (this.getMedia() > 7) {
            return "Aprovado";
        } else {
            return "Reprovado";
        }
    }
}
