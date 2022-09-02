nome = input('Vendedor(a): ')
quantcarros = int(input('Quantos carros você vendeu? '))
totalvendas = float(input('Qual o valor total das suas vendas? '))

comissao = quantcarros*200
valorvenda = totalvendas - (totalvendas * 5 / 100)
salario = float(comissao + valorvenda + 1000)

print(f'Vendedor(a) {nome} seu salário esse mês é: {salario}')