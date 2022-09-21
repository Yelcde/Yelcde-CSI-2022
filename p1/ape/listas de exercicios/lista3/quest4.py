comparador = 0
for i in range(1, 6):
    num = int(input('Me dê um número: '))
    if (num > comparador):
        comparador = num
print(f'O maior número é: {comparador}')