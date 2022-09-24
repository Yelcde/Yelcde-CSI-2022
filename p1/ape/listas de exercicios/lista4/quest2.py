print('Bem vindo ao programa de média\nSe quiser parar, digite 999')
print('='*30)
cont = 0
soma = 0
soma_media = 0
while soma_media != '999':
    soma_media = float(input('Digite um número: '))
    if (soma_media == 999):
        break
    soma += soma_media
    cont += 1
media = soma//cont
print(f'A média dos números concedidos a mim é {media}')