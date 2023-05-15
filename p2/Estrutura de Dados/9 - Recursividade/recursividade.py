# O que devo saber para criar uma função recursiva?
# (1) Identique um padrão geral de comportamento do seu problema
#     base * base * base (indicado pelo expoente)
# (2) Identificar os casos base
#    Qualquer base elevada ao valor zero é igual a 1
def potencia(base,expoente):
    # condição de parada
    return 0 if expoente == 0 else 1 + potencia(base,expoente-1)
    # if expoente == 0:
    #     return 0
    # else:
    #     return 1 + potencia(base, expoente-1)

def fib(n):
    if n ==0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def f1(n,k):
    if n == k:
        return
    else:
        f1(n+1,k-2)
        print(n)


def reverso(s):
    if len(s)==0:
        return
    print(s[0],end='')
    reverso(s[1:])
    
# programa principal
reverso('Recursividade com strings')
print()
f1(4,10)
# print(potencia(2,3))
# print(fib(2))