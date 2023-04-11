# import os

# print('Sou processo principal (pai). Meu PID é: ', os.getpid())

# escolha = input('\nDigite 1 para criar um novo processo, outra tecla qualquer para sair:' )

# if escolha == '1':
#     pid = os.fork()
#     if pid == 0:
#         print('Johnner Yelcde da Cruz Castro')
#     elif pid > 0:
#         print('Sou pai. Meu PID é:' + str(os.getpid()) + 
#           " Meu filho é: " + str(pid))
# else:
#     exit()

# Por algum motivo que desconheço o os.fork() não funciona