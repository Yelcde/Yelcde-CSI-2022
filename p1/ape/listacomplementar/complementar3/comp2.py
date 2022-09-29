n = int(input('Me dê um número inteiro: '))
primo = ''
for i in range(1, n):
  resto = n % i
  if (resto == 0):
    primo = primo + str(i)
  else:
    continue
print(primo)

# Não terminada