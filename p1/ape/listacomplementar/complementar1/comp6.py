valorretirada = float(input('Qual o valor que você quer retirar? '))
retirada = valorretirada
b50 = valorretirada // 50
b10 = (valorretirada % 50) // 10
b5 = ((valorretirada % 50) % 10) // 5
b1 = ((valorretirada % 50) % 10) % 5

print(f'Você vai retirar {b50} B$ 50, {b10} B$ 10, {b5} B$ 5 e {b1} B$ 2')