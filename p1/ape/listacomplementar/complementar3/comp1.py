num = int(input('Me dê um número inteiro maior ou igual a 2: '))
contador = 0
num_destrinchado = 1
resultado = 0
while num >= resultado:
    resultado = contador + num_destrinchado
    if (resultado == 1):
        contador = 0
    elif (resultado > 1):
        contador += 1
    num_destrinchado += 1
    print(resultado)