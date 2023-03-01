function sum(a, b) {
    return a + b;
}

// call function
// console.log(sum(1));
// console.log(sum(1, 1));
// console.log(sum(1, 1,1));

//rest param
function add (...values){
    let sum = 0;

    for (const value of values){
        sum += value;
    }

    return sum
}

// console.log(add(1));
// console.log(add(1, 2));
// console.log(add(1, 2, 3));

//default param
function calc(value1, value2, operator = '+'){
    switch (operator) {
        case '+':
          return value2 + value1;
        case '-':
          return value2 - value1;
        default:
          return 'Invalid Operator';
    }
}

console.log(calc(1, 2));
console.log(calc(1, 2, '-'));
console.log(calc(1, 2, 'f'));