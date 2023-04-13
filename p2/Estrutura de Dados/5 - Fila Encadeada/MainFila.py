from FilaEncadeada import Fila,FilaException

fila = Fila()

for i in range(1,6):
    fila.enfileira(i*10)
print(fila)

print(fila)
print('Editor de Listas')
print('='*24)
print('''
1 - Mostrar Menu
2 - Tamanho
3 - Inserir
4 - Remover
5 - Exibir Elemento
6 - Procurar valor
7 - Modificar
8 - sair
    ''')
while True:
    opcao = input('Digite sua opção: ')

    if opcao == '1':
        print('''
1 - Mostrar Menu
2 - Tamanho
3 - Inserir
4 - Remover
5 - Exibir Elemento
6 - Procurar valor
7 - Modificar
8 - sair
        ''')    
    
    elif opcao == '2':
        print(f'O tamanho da fila é: {len(fila)}\n')
    
    elif opcao == '3':
        valor = int(input('Qual o valor que você quer inserir? '))
        fila.enfileira(valor)
        print('Valor inserido!\n')
        
    elif opcao == '4':
        pos = int(input('Me dê a posição do elemento a ser excluido: '))
        carga = fila.desenfileira(pos)
        print(f'Valor {carga} removido com sucesso!\n')

    elif opcao == '5':
        pos = int(input('Me dê a posição do elemento: '))
        elemento = fila.elemento(pos)
        print(elemento)

    elif opcao == '6':
        valor = int(input('Me dê valor do elemento: '))
        elemento = fila.busca(valor)
        print(elemento)
    
    elif opcao == '7':
        pos = int(input('Me dê a posição que você quer inserir um novo valor: '))
        valor = int(input(f'Qual o novo valor que você quer inserir na posição {pos}? '))
        novoValor = fila.modificaValor(pos, valor)
        print(novoValor)
        print(fila)

# print('Elemento(): ', fila.elemento(3))
# print('busca(): ', fila.busca(20))

# try:
#     for i in range(10):
#         print(fila.desenfileira())
# except FilaException as fe:
#     print(fe)