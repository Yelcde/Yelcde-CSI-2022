import random

# inicialização de variaveis

nlin = 2
ncol = 3

# criação das matrizes nulas

a = [[None]*ncol for i in range(nlin)]
b = [[None]*ncol for i in range(nlin)]
c = [[None]*ncol for i in range(nlin)]

# geração aleatoria da matriz A

for i in range(nlin):
    for j in range(ncol):
        a[i][j] = random.randint(1,10)

# geração da matriz B

for i in range(nlin):
    for j in range(ncol):
        b[i][j] = random.randint(1,10)

# calculo da matriz A + B

for i in range(nlin):
    for j in range(ncol):
        c[i][j] = a[i][j] + b[i][j]

# impressão da matriz A

print('Matriz A')
for i in range(nlin):
    for j in range(ncol):
        print(f'{a[i][j]:3}', end='')
    print()

# impressão da matriz B

print('Matriz B')
for i in range(nlin):
    for j in range(ncol):
        print(f'{b[i][j]:3}', end='')
    print()
    
# impressão da matriz C

print('Matriz C')
for i in range(nlin):
    for j in range(ncol):
        print(f'{c[i][j]:3}', end='')
    print()