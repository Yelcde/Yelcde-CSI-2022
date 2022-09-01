nome = input('Qual o seu nome? ')
conceito = input('Qual o seu conceito? ').upper()
if (conceito == 'A'):
  print(f'Você, aluno(a) {nome}, é um aluno fortemente recomendado')
elif (conceito == 'B' or conceito == 'C'):
  print(f'Você, aluno(a) {nome}, é um aluno recomendado')
elif (conceito == 'D'):
  print(f'Você, aluno(a) {nome}, é um aluno não recomendado')
else:
  print('Escreva um dos conceitos existentes: A, B, C ou D')