const lista = [1, 2, 3, 4, 5, 6]

let soma = sum(lista)

function sum(array) {
    let result = 0;
    for (const index in array) {
        result += array[index]
    }
    return result
}

console.log(soma)