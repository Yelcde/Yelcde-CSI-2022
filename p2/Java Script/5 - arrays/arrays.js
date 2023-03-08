// Criando Arrays e, JS
let array = [10, 5];
let arrayAsObject = new Array(10, 5);

// Checando se é um array
console.log(arrayAsObject.push(20));
console.log(typeof array);
console.log(Array.isArray(arrayAsObject))

array[0] = 2;
console.log(array[0]);

array = [10, 5, 'LS', {nome: 'Francisco', disciplina: "LS"}];
console.log(array[3].disciplina);
// Acessando o [3] e especificando que é a disciplina
console.log(array[4][1]);

let array1 = [1, 2, 3];
let array2 = [4, 5, 6];

// Joyn é um separador, que serve para separar os itens de um array
console.log(array1, join(' - '));

// array = [array1, array2];
array = [...array1, ...array2];
// array = [1, 2, 3, ...array2];
// array = [1, 2, 3, 4, 5, 6, 7];
