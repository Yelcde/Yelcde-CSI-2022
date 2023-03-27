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

for (const i in companies) {
    companies[i].kind = 'Internet company'
}

function show(companies) {
    for (const company of companies) {
        console.log(company.nome.padEnd(15, '.'), company.fundacao)
    }
}

// console.log(companies)
show(companies)

// console.log(JSON.stringify(companies, null, 2))