print('Escolha o código e a quantidade do seu lanche:')
print('H = Hamburguer\nC = Cheese Burguer\nB = Cheese Bacon\nF = Cheese Frango')
print('Se já terminou, digite x')

h = 5
c = 6
b = 7
f = 4
pedido = 0
while pedido != 'x':
    pedido = input('Qual o seu pedido? ').upper()
    if (pedido == 'X'):
        break
    if (pedido == 'H'):
        lanche = h
    elif (pedido == 'C'):
        lanche = c
    elif (pedido == 'B'):
        lanche = b
    elif (pedido == 'F'):
        lanche = f
        
    quantidade = int(input('Qual a quantidade? '))
    if (quantidade > 0 and lanche == h):
        preço = quantidade * lanche
    elif (quantidade > 0 and lanche == c):
        preço = quantidade * lanche
    elif (quantidade > 0 and lanche == b):
        preço = quantidade * lanche
    elif (quantidade > 0 and lanche == f):
        preço = quantidade * lanche
    str(preço)
    resultado = preço
    
print(resultado)
    