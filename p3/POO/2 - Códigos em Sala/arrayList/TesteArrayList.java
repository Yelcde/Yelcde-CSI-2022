package arrayList;

import java.util.ArrayList;

public class TesteArrayList {
    public static void main(String[] args) {
        int[] numeros = new int[4];
        numeros[0] = 8;
        numeros[1] = 2;
        numeros[2] = 9;
        numeros[3] = 2;

        ArrayList<Integer> lista = new ArrayList<> ();
        lista.add(1);
        lista.add(2);
        lista.add(3);
        lista.add(4);
        // System.out.println(lista.size());
        // System.out.println(lista.get(2));
        // System.out.println(lista.get(3));
        // System.out.println(lista.get(0));

        lista.remove(0);
        System.out.println(lista.size());
    }
}
