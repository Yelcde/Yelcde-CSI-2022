num = 1
maior = 0
menor = 999999999999999999999999999999999999999999999999999999
while num != 0:
    num = int(input("Me dê um número inteiro: "))
    if (num == 0):
        break
    if (num > maior):
        maior = num
    elif (num < menor):
        menor = num
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
