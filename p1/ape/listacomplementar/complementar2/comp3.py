ano = int(input('Digite o ano que você quer saber se é bissexto: '))
if (ano % 4 == 0):
  print(f'O ano é bissexto!')
elif (ano % 4 != 0):
  print(f'O ano não é bissexto!')