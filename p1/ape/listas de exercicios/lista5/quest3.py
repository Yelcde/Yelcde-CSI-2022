import random

vetor_quant = int(input('Me diga qual o tamanho da lista: '))
index = []

vetor = [None]*vetor_quant
for i in range(vetor_quant):
    vetor[i] = random.randint(1, vetor_quant)

k = int(input('Me dê um número inteiro: '))

quant = 0
for i in range(vetor_quant):
    if (k == vetor[i]):
        quant += 1
        index.append(i)
        
index_quant = len(index)
for i in range(index_quant):
    index[i] = index[i] + 1

if (quant > 0):
    print(f'O número {k} lista {vetor} aparece {quant} vezes nos indices {index}')
else:
    print(f'O número {k} lista {vetor} aparece 0 vezes')