n = int(input('Me dê um número inteiro que lhe darei o quadrado perfeito: '))
for i in range(n, 1, -1):
    quadrado = i ** 2
    if (quadrado < n or quadrado == n):
        print(f'O quadrado perfeito de {n} é {quadrado}')
        break