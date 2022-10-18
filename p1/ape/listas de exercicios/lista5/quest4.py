vetor = [None]*10
par = []
impar = []

um = 1

for i in range(10):
    vetor[i] = int(input(f'{um}/10 Me dê um número: '))
    if (i % 2 == 0):
        par.append(vetor[i])
    else:
        impar.append(vetor[i])
    um += 1

print(par)
print(impar)