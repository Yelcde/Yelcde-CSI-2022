salario_minimo = 1200
total_vendas = float(input('Qual o total das suas vendas? '))
comissao = (total_vendas * 5)/100
if (comissao >= salario_minimo):
  print(f'Seu salário será de {comissao} R$')
else:
   print(f'Seu salário será de {salario_minimo} R$')