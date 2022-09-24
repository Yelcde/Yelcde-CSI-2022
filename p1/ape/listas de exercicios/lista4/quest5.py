print('Me dê um número e direi se ele é par ou não!\nQuer sair? Digite Sair\nQuer continuar? Digite Continuar')
flow = 0
while flow != 'sair':
    num = int(input('Me dê um número inteiro: '))
    if (num % 2 == 0):
        print(f'{num} é par!')
    elif (num % 2 != 0):
        print(f'{num} é impar!')
    flow = input('Quer continuar? ').upper()
    if (flow == 'SAIR'):
        break
    elif (flow == 'CONTINUAR'):
        continue
print('Fim do programa')