const lista = [2, 2, 2]

let soma = product(lista)

function product(array) {
    let result = 1;
    for (const index in array) {
        result *= array[index]
    }
    return result
}

console.log(soma)