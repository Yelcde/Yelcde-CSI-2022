vetor_quant = int(input('Me diga o tamanho do Vetor: '))
vetor = [None]*vetor_quant

for i in range(vetor_quant):
    vetor[i] = int(input('Me diga um número: '))

vetor = list(reversed(vetor))
print(vetor)