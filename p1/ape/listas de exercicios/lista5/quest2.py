import random

vetor = [None]*30
for i in range(30):
    vetor[i] = random.randint(1, 30)

k = int(input('Me dê um número inteiro: '))

quant = 0
for i in range(30):
    if (k == vetor[i]):
        quant += 1
        
print(f'O número {k} aparece na lista {quant} vezes')
print(vetor)