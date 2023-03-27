const companies = [
    {
        nome: "Amazon", 
        fundacao: 1994, 
        atuacao: 'E-Commerce, Cloud',
        kind: '',
    },
    
    {
        nome: 'Facebook', 
        fundacao: 2004, 
        atuacao: 'Social',
        kind: '',
    },
    
    {
        nome: 'Alphabet Inc', 
        fundacao: 2015, 
        atuacao: 'Search, Cloud, Advertising',
        kind: '',
    },
]

// Adicionando mais um item ao objeto
for (const i in companies) {
    companies[i].kind = 'Internet company'
}

function show(companies) {
    // Vendo qual empresa tem o maior nome
    let biggest = 0
    for (const company of companies) {
        if (company.nome.length > biggest){
            biggest = company.nome.length
        }
    }
    
    for (const company of companies) {
        console.log(company.nome.padEnd(biggest+3, '.'), company.fundacao)
    }
}

// console.log(companies)
show(companies)