const inputHTML = document.querySelector('.quantity');
const button = document.querySelector('button');
const printHTML = document.querySelector('.list');

function listGeneration(number)
{
    for (let i = 1; i <= number; i++) {
        printHTML.innerHTML += `<li>Item ${i}</li>`
    }
};

button.addEventListener('click', () => {
    printHTML.innerHTML = ""
    const number = inputHTML.value;
    listGeneration(number);
})