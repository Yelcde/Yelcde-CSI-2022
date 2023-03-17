const lista = [1, 2, 3, 4, 5, 6]

let soma = sumOdds(lista)

function sumOdds(array) {
    let result = 0;
    for (const index in array) {
        if (array[index] % 2 != 0){
            result += array[index]
        } 
    }
    return result
}

console.log(soma)