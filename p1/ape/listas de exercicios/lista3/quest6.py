n = int(input('Me dê um número inteiro para eu achar os multiplos: '))
x = int(input('Me dê um número para o inicio do intervalo: '))
y = int(input('Me dê um número para o fim do intervalo: '))
if (x > y):
    print(f'[ERRO] O primeiro número {x} é maior que o segundo número {y}. Coloque o primeiro número menor que o segundo.')
elif (x < y):
    for i in range(x, y+1):
        multi = i * n
        print(f'Na posição {i} do intervalo o multiplo é {multi}')
        print('=' * 45)
else: 
    print('[ERRO] Coloque um número inteiro!')