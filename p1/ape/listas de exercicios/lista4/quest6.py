altura_ze = 1.10
altura_chico = 1.50
ano = 0
while altura_ze <= altura_chico:
    altura_ze = altura_ze + 0.03
    altura_chico = altura_chico + 0.02
    ano += 1
print(f'Em {ano} anos, Zé vai passar de Chico')