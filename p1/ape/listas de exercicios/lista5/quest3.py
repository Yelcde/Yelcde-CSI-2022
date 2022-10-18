import random

vetor_quant = int(input('Me diga qual o tamanho da lista: '))
vetor_index = [None]
pos = -1

vetor = [None]*vetor_quant
for i in range(vetor_quant):
    vetor[i] = random.randint(1, vetor_quant)

k = int(input('Me dê um número inteiro: '))

quant = 0
for i in range(vetor_quant):
    if (k == vetor[i]):
        quant += 1
        vetor_index[pos+1] = i
        
print(f'O número {k} aparece na lista {quant} vezes')
print(vetor)
print(vetor_index)