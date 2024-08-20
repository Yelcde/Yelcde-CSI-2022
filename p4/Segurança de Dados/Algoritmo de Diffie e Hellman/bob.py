def calcula_b(num_primo, base, x):
    return (base**x) % num_primo 

def calcula_segredo_b(num_primo, base, a):
    y = int(input(': '))
    b = calcula_b(num_primo, base, y)
    segredo_b = (a ** y) % num_primo
    print(segredo_b)
    return b