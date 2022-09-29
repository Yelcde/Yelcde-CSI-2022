num_1 = int(input('Me dê um número inteiro: '))
num_2 = int(input('Me dê outro número inteiro: '))

resto = -1
mdc = 0

print(f'O MDC de {num_1} e {num_2} é {mdc} e a sequência é: {num_1} {num_2} ', end='')

while resto != 0:
  resto = num_1 % num_2
  if (resto != 0):
    mdc = resto
  elif (resto == 0):
    break
  num_1 = num_2
  num_2 = resto
  print(resto, end=' ')