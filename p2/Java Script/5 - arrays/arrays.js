// Create array with values

const values = [1, 2, 3];
console.log(values);

// Create empty array

const numbers = [];
numbers.push(1); // Adiciona o valor
console.log(numbers);

numbers.unshift(0); // Coloca o valor no inicio
console.log(numbers);

numbers[2] = 2;
console.log(numbers);

// Multiple types

const person = ['John', 30, true, ['john@gmail.com']];

// Destruction array

// const name = person[0];
// const age = person[1];
// const [name, age] = person
const [ ,age] = person;
const [ , , ,[email]] = person;

// React
// const [name, setName] = useState('');

console.log(age);

// Spread operator

const students = [...person, "TSI"];

// Interation

for (let flag = 0; flag < numbers.length; flag++){
    console.log(numbers[flag]);
}

for (const numbers in numbers){
    console.log(numbers)
}

for (const numbers of numbers){
    console.log(numbers)
}