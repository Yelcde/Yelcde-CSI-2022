pessoas = int(input('São quantas pessoas? '))
m = 0
f = 0
for i in range(1, pessoas+1):
    sexo = input('Qual o seu sexo [M/F]? ').upper()
    if (sexo == 'M'):
        m += 1
    elif (sexo == "F"):
        f += 1
    else:
        print('[ERRO!] Escreva [M/F]')
        
# Porcentagem
pm = (m/pessoas)*100
pf = (f/pessoas)*100
print(f'A porcentagem de homens é {pm}%')
print(f'A porcentagem de mulheres é {pf}%')