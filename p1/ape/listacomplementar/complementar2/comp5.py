import math
a = float(input('Me dê o A da equação de segundo grau: '))
b = float(input('Me dê o B da equação de segundo grau: '))
c = float(input('Me dê o C da equação de segundo grau: '))
D = (b**2 - 4*a*c)
if (D < 0):
  print('Não existes raizes para equações com o Delta menor que 0')
else:
  x1 = ((-b + math.sqrt(D))/ 2*a)
  x2 = ((-b - math.sqrt(D))/ 2*a)
  print(f'As raizes são {x1} e {x2}')