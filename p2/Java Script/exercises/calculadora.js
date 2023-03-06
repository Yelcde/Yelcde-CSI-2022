function soma(num1, num2){
    return num1 + num2;
}

function sub(num1, num2){
    return num1 - num2;
}

function mult(num1, num2){
    return num1 * num2;
}

function div(num1, num2){
    return num1 / num2;
}

let number1 = 10;
let number2 = 2;
let operador = '/';

switch (operador) {
    case "+":
        result = console.log(soma(number1, number2))
        break;
    case "-":
        result = console.log(sub(number1, number2))
        break;
    case "*":
        result = console.log(mult(number1, number2))
        break;
    case "/":
        result = console.log(div(number1, number2))
        break;
}