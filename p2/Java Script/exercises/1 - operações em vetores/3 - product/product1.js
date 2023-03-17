const lista = [1, 2, 3]

let soma = product(lista)

function product(array) {
    let result = 1;
    for (const index in array) {
        result *= array[index]
    }
    return result
}

console.log(soma)