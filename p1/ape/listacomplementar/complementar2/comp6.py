primeira_nota = float(input('Qual foi sua primeira nota: '))
segunda_nota = float(input('Qual foi sua segunda nota: '))
media = (primeira_nota + segunda_nota)/2
if (media >= 7):
  print('Parabéns! Você passou para a segunda etapa!')
  terceira_nota = float(input('Qual foi a sua nota na segunda etapa: '))
  if (terceira_nota >= 8):
    print('Parabéns! Você passou no concurso')
  else:
    print('Você foi bem até aqui, mas não foi dessa vez. Se inscreva no próximo concurso!')
else:
  print('Não foi dessa vez! Se inscreva no próximo concurso!')