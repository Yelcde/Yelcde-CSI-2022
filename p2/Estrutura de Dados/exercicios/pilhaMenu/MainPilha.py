from PilhaEncadeada import Pilha, PilhaException

p = Pilha()

# Testando Empilha e Desempilha
# p.empilha(10)
# print(p)
# p.empilha(20)
# print(p)
# retirado = [p.desempilha()]
# retirado += [p.desempilha()]
# print(p)
# print(retirado)

for i in range (1,11):
    p.empilha(i*10)

print(p)

try:
    while(True):
        print('desempilha: ', p.desempilha())
except PilhaException as pe:
    print(pe)

dado = p.topo()
print(dado)
