num1 = float(input('Qual o primeiro número: '))
num2 = float(input('Qual o segundo número: '))
print('Adição -> +\nSubtração -> -\nMultiplicação -> x\nPotenciação -> *\nDivisão -> /\nResto da Divisão -> %')
operador = input('Qual operador você quer usar? ').lower()
if (operador == '+'):
  conta = num1 + num2
  print(f'O resultado da conta é {conta}')
elif (operador == '-'):
  conta = num1 - num2
  print(f'O resultado da conta é {conta}')
elif (operador == 'x'):
  conta = num1 * num2
  print(f'O resultado da conta é {conta}')
elif (operador == '*'):
  conta = num1 ** num2
  print(f'O resultado da conta é {conta}')
elif (operador == '/'):
  conta = num1 / num2
  print(f'O resultado da conta é {conta}')
elif (operador == '%'):
  conta = num1 % num2
  print(f'O resultado da conta é {conta}')
else:
  print('[ERRO] Escolha um operador da lista!')