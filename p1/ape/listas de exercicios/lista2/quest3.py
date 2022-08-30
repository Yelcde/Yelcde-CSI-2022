num1 = int(input('Me dê um número: '))
num2 = int(input('Me dê outro número: '))
num3 = int(input('Me dê mais um número: '))
if (num1 > num2 and num1 > num3):
    print(f'{num1} é o maior número entre {num1}, {num2} e {num3}')
elif (num2 > num1 and num2 > num3):
    print(f'{num2} é o maior número entre {num1}, {num2} e {num3}')
else:
    print(f'{num3} é o maior número entre {num1}, {num2} e {num3}')