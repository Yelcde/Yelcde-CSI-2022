caractere = input('Digite qualquer tecla do seu teclado que imprima algo: ').lower()
if (caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u'):
    print('Você escreveu uma vogal')
elif (caractere == 'q' or caractere == 'w' or caractere == 'r' or caractere == 't' or caractere == 'y' or caractere == 'p' or caractere == 's' or caractere == 'd' or caractere == 'f' or caractere == 'g' or caractere == 'h' or caractere == 'j' or caractere == 'k' or caractere == 'l' or caractere == 'ç' or caractere == 'z' or caractere == 'x' or caractere == 'c' or caractere == 'v' or caractere == 'b' or caractere == 'n' or caractere == 'm'):
    print('Você escreveu uma consoante')
elif (caractere == '1' or caractere == '2' or caractere == '3' or caractere == '4' or caractere == '5' or caractere == '6' or caractere == '7' or caractere == '8' or caractere == '9' or caractere == '0'):
    print('Você escreveu um número')
else:
    print('Você escreveu um caractere especial')