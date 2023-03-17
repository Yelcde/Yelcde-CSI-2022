const lista = [2, 2, 2]

let soma = sum(lista)

function sum(array) {
    let result = 0;
    for (const index in array) {
        result += array[index]
    }
    return result
}

console.log(soma)