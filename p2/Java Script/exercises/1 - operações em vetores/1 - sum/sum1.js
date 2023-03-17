const lista = [1, 2, 3]

let soma = sum(lista)

function sum(array) {
    let result = 0;
    for (const index in array) {
        result += array[index]
    }
    return result
}

console.log(soma)