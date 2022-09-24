print('Vou mostrar sua situação em relação as suas notas\nSe quiser parar, digite 0 na matricula')
media = 0
matricula = 1
while matricula != 0:
    matricula = int(input('Qual a matricula do aluno? '))
    if (matricula == 0):
        break
    aluno = input('Qual o nome do aluno? ')
    prova_1 = float(input('Qual a nota da primeira prova do aluno? '))
    prova_2 = float(input('Qual a nota da segunda prova do aluno? '))
    media = (prova_1 + prova_2)/2
    if (media >= 7):
        print(f'O aluno {aluno}, com a matricula {matricula}, com média {media}, está aprovado!')
    else:
        print(f'O aluno {aluno}, com a matricula {matricula}, com média {media}, está reprovado!')
if (matricula == 0):
    print('Até a próxima!')
if (matricula == 0 and media == 0):
    print('Entrou em mim por engano? Tudo bem! Até a próxima!')