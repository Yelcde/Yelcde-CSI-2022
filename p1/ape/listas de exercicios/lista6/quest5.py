import random

# tamanho da matriz

nlin = 20
ncol = 4

# criação da matriz

notas = [[None]*ncol for i in range(nlin)]

# preenchendo notas dos alunos

for i in range(nlin):
    notas_a = 0
    for j in range(ncol):
        notas[i][j] = random.randint(1,10)
        notas_a += notas[i][j]
    media = notas_a // 3
    notas[i][j] = media
    
        
for i in range(nlin):
    for j in range(ncol):
        print(f'{notas[i][j]:3}', end='')
    print()

# NÃO TERMINADA