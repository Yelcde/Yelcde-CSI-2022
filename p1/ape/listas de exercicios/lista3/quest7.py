num = int(input('Me dê um número: '))

primo = 1
nao_primo = 0

for i in range(2, 101):
    resto = num % i
    if (resto == 0):
        primo += 1
    else:
        nao_primo += 1
        
if (primo == 2):
    print(f'O número {num} é primo')
elif(nao_primo > 0):
    print(f'O número {num} não é primo')