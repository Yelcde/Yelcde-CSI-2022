import random

# definindo tamanho da matriz

nlin = 3
ncol = 5

# criando matriz A

matriz_a = [[None]*ncol for i in range(nlin)]

# criação da matriz B

matriz_b = [[None]*ncol for i in range(nlin)]

# preenchendo aleatoriamente a matriz A

for i in range(nlin):
    for j in range(ncol):
        matriz_a[i][j] = random.randint(1,20)
        
# preenchendo aleatoriamente matriz B

for i in range(nlin):
    for j in range(ncol):
        matriz_b[i][j] = random.randint(1,20)
       
# mostrando matriz A

print('Matriz A')
for i in range(nlin):
    for j in range(ncol):
        print(f'{matriz_a[i][j]:5}', end='')
    print()

# preenchendo matriz B

for i in range(nlin):
    for j in range(ncol):
        matriz_b[i][j] = matriz_a[i][j]
        
# mostrando matriz B

print('Matriz B')
for i in range(ncol):
    for j in range(nlin):
        print(f'{matriz_a[j][i]:5}', end='')
    print()