import java.util.ArrayList;
import java.util.Arrays;

public class Estacionamento {
    private String[] placas;

    public Estacionamento(int n) throws Exception {
        if (n < 1) {
            throw new Exception("Número Negativo");
        }
        ;

        placas = new String[n];
        for (int i = 0; i < placas.length; i++) {
            placas[i] = "livre";
        }
    }

    public void entrar(String placa, int vaga) throws Exception {
        //se vaga não existe, lança a exceção “vaga inexistente”
        //armazena a placa na vaga especificada
        if (vaga < 1 || vaga > placas.length) {
            throw new Exception("Vaga inexistente! Por favor digite uma vaga entre 1 e " + placas.length);
        }

        if (!placas[vaga - 1].equals("livre")) {
            throw new Exception("Vaga já preenchida! Escolha outra.");
        }

        placas[vaga - 1] = placa;
    }

    public int entrar(String placa) throws Exception {
        //se não há vaga disponivel, lança a exceção “lotado”
        //armazena a placa na primeira vaga disponivel encontrada
        //retorna a vaga encontrada
        if (!Arrays.asList(placas).contains("livre")) {
            throw new Exception("O estacionamento está lotado!");
        }
        
        int vaga = 0;
        for (int i = 0; i < placas.length; i++) {
            if (placas[i].equals("livre")) {
                placas[i] = placa;
                vaga = i+1;
                break;
            }
        }
        return vaga;

    }

    public ArrayList<Integer> listarLivres() {
    //adiciona na lista aux as posições do array que estão “livre”
        ArrayList<Integer> aux = new ArrayList<>();
        for (int i = 0; i < placas.length; i++) {
            if (placas[i].equals("livre")) {
                System.out.println(placas[i]);
                aux.add(i+1);
            }
        }
        return aux;
    }
}

