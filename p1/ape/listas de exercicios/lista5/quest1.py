n = int(input('Qual o tamanho do Vetor? '))
k = int(input('Me dê outro para multiplicar: '))

a = [None]*n
b = [None]*n

for i in range(n):
    a[i] = int(input(f'Me dê um número: '))
    b[i] = a[i]*k
print(f'O vetor A = {a} multiplicado com a variavel {k} dá A = {b}')