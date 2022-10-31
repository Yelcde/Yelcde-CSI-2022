import random

# leitura da ordem da matriz

ordem = int(input('Me dê o tamanho da matriz: '))

# criação da matriz com valores nulos

a = [[None]*ordem for i in range(ordem)]
b = [[None]*ordem for i in range(ordem)]

# geração da matriz A com valores aleatorios

for i in range(ordem):
    for j in range(ordem):
        a[i][j] = random.randint(1, 20)

# geração da matriz B com valores aleatorios

for i in range(ordem):
    for j in range(ordem):
        b[i][j] = a[i][j] + i + j
        if (i == j):
            b[i][j] = 0
        elif ((i + j) == (ordem - 1)):
            b[i][j] = 0

# imprimir a matriz A

print('Matriz A')
for i in range(ordem):
    for j in range(ordem):
        print(f'{a[i][j]:3}', end='')
    print()
    
# imprimir matriz B

print('Matriz B')
for i in range(ordem):
    for j in range(ordem):
        print(f'{b[i][j]:3}', end='')
    print()