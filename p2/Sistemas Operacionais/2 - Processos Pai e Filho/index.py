# import os
# while True:
#     num1 = int(input('Primeiro número: '))
#     num2 = int(input('Segundo número: '))
#     if (num2 < num1):
#         print('Escreva o primeiro número menor que o segundo')
#     elif (num1 == num2):
#         print('Escreva o primeiro número menor que o segundo')
#     elif (num1+1 == num2):
#         print('Escreva o primeiro com um espaço de pelo menos 2 números para o segundo')
#     else: 
#         print('\n')
#         break


# ret = os.fork()
# if (ret > 0):
#     os.wait()
#     print('Sou o pai, esperei meu filho processar e agora vou mostrar o resultado!\n')
#     with open("saida.txt", "r") as arquivo:
#         print(arquivo.read())
# else:
#     print('Sou o filho e enquanto meu pai espera vou processar os pares entre os números que você me deu!\n')
#     print('[Processando...]\n')
#     with open("saida.txt", "w") as arquivo:
#         for i in range(num1, num2+1):
#             if ((i % 2) == 0):
#                 arquivo.write(str(i) + '\n')

# Por algum motivo que desconheço o os não funciona