print('Se quiser parar, digite 0')
idade = 1 
cont = 0
soma = 0
entre = 0
mais_jovem = 999999999999
while (idade != 0):
    idade = int(input('Qual a idade do visitante? '))
    if (idade == 0):
        break
    soma += idade
    if (idade >= 18 and idade <= 21):
        entre += idade
    if (idade < mais_jovem):
        mais_jovem = idade
    cont += 1

media = soma/cont
porcentagem = (entre/soma)*100
print(f'A média de idade dos visitantes é {media:.0f} anos')
print(f'A porcentagem de pessoas com idade entre 18 e 21 anos é {porcentagem:.0f}%')
print(f'A pessoa mais jovem é {mais_jovem} anos')