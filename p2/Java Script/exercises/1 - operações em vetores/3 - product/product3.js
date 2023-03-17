const lista = [1, 2, 3, 4, 5, 6]

let soma = product(lista)

function product(array) {
    let result = 1;
    for (const index in array) {
        result *= array[index]
    }
    return result
}

console.log(soma)