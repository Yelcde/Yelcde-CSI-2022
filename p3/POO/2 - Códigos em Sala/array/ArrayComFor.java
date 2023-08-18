public class ArrayComFor {
    public static void main(String[] args) {
        int[] numeros = new int[4];
        numeros[0] = 8;
        numeros[1] = 2;
        numeros[2] = 9;
        numeros[3] = 2;

        // for (int i = 0; i < numeros.length; i++){
        //     System.out.println(numeros[i]);
        // }
        for(int n : numeros)
            System.out.println(n);
    }
}


// Array usando os próprios elementos (sem indice)
// for(int n : numeros)
//     System.out.println(n);