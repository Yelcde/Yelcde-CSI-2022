import random

# leitura da ordem da matriz

ordem = int(input('Me dê o tamanho da matriz: '))

# criação da matriz com valores nulos

a = [[None]*n for i in range(ordem)]
b = [[None]*n for i in range(ordem)]

# geração da matriz com valores aleatorios

for i in range(n):
    for j in range(n):
        m[i][j] = random.randint(1, 20)

# imprimir a matriz

print('Matriz')
for i in range(n):
    for j in range(n):
        print(f'{m[i][j]:3}', end='')
    print()

# diagonal

print('Diagonal')
for i in range(n):
    for j in range(n):
        if (i == j):
            print(f'{m[i][j]:3}', end='')
    print('', end='')

NÃO TERMINADA