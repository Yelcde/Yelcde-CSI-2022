peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
massa = peso / (altura**2)
if (massa < 20):
  print('Você precisa engordar!')
elif (massa >= 20 or massa <=26):
  print('Você é normal! Continue assim!')
elif (massa > 26 or massa < 30):
  print('Você está obeso! Emagreça!')
elif (massa >= 30):
  print('Você é obeso mórbido! Emagreça URGENTE')