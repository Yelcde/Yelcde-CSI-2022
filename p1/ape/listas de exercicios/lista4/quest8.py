print('Escolha o código e a quantidade do seu lanche:')
print('H = Hamburguer\nC = Cheese Burguer\nB = Cheese Bacon\nF = Cheese Frango')
print('Se já terminou, digite x')

PRECO_H = 5
PRECO_C = 6
PRECO_B = 7
PRECO_F = 4
pedido = 0
preco = 0

while pedido != 'x':
    pedido = input('Qual o código do seu lanche? ').upper()
    if (pedido == 'X'):
        break
    if (pedido != 'H' and pedido != 'C' and pedido != 'B' and pedido != 'F'):
        print('Digite uma letra válida!')
        continue
    quantidade = int(input('Qual a quantidade? '))
    if (pedido == 'H'):
        preco += PRECO_H * quantidade
    elif (pedido == 'C'):
        preco += PRECO_C * quantidade
    elif (pedido == 'B'):
        preco += PRECO_B * quantidade
    elif (pedido == 'F'):
        preco += PRECO_F * quantidade
    
print(f'O total a pagar é {preco},00 R$')