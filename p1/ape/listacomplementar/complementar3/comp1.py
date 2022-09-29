num = int(input('Me dê um número inteiro maior ou igual a 2: '))

a = 0
b = 1

print('Sequencia: ', a, b, end=' ')

for i in range(3, num+1):
    c = a + b
    print(c, end=' ')
    a = b
    b = c