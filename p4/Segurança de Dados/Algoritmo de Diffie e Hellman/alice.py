from bob import calcula_segredo_b

def calcula_a(num_primo, base, x):
    return (base**x) % num_primo 

def pega_b(num_primo, base, a):
    b = calcula_segredo_b(num_primo, base, a)
    return b

def calcula_segredo_a(num_primo, b, x):
    return (b**x) % num_primo

num_primo = 47
base = 3
x = int(input(': '))
a = calcula_a(num_primo, base, x)
b = pega_b(num_primo, base, a)
segredo_a = calcula_segredo_a(num_primo, b, x)
print(segredo_a)