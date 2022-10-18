vetor_quant = int(input('Me diga o tamanho do Vetor: '))
vetor = [None]*vetor_quant

for i in range(vetor_quant):
    vetor[i] = int(input('Me diga um número: '))

maior = max(vetor)
menor = min(vetor)

print(f'O maior e o menor número do Vetor {vetor} são {maior} e {menor}')