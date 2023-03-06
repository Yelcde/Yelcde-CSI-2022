function verTriangulo(l1, l2, b){
    if ((l1 + l2) == b || (l1 + l2) > b) {
        return "Isso não é um triangulo";
    } else if (l1 < 0 || l2 < 0 || b < 0) {
        return "Isso não é um triangulo";
    } else if (l1 == l2 && l1 == b) {
        return "Esse triangulo é equilateral";
    } else if ((l1 == l2 && l1 != b) || (l1 == b && l1 != l2) || (l2 == b && l2 != l1)) {
        return "Esse triangulo é isosceles";
    } else if (l1 != l2 && l2 != b && b !=l1) {
        return "Esse triangulo é escaleno";
    } else {
        return "Isso não é um triangulo";
    } 
}

let lado1 = 2;
let lado2 = 4;
let base = 2;

triangulo = console.log(verTriangulo(lado1, lado2, base))
console.log(triangulo)


//    Entrada       |   Saída
//   --------------------------------
//    2, 2, 2	    |   equilateral
//    10, 10, 10    |   equilateral
//    3, 4, 4	    |   isosceles
//    4, 3, 4	    |   isosceles
//    4, 4, 3	    |   isosceles
//    10, 10, 2     |   isosceles
//    3, 4, 5	    |   scalene
//    10, 11, 12    |   calene
//    5, 4, 2	    |   scalene
//    0, 0, 0	    |   none
//    3, 4, -5      |   none
//    1, 1, 3	    |   none
//    2, 4, 2	    |   none