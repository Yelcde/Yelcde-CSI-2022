nome = input('Qual o seu nome? ')
sexo = input('Qual o seu sexo? [M/F] ').upper()
if (sexo == 'M'):
  print(f'Olá senhor {nome}')
elif (sexo == 'F'):
  print(f'Olá senhora {nome}')