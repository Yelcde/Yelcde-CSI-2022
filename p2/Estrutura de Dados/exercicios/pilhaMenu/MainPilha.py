from PilhaEncadeada import Pilha, PilhaException

p = Pilha()

for i in range (1,11):
    p.empilha(i*10)

print(f'{p}\n')

busca = p.busca(20)
print(f'{busca}\n')

elemento = p.elemento(5)
print(f'{elemento}\n')

topo = p.topo()
print(f'{topo}\n')



# try:
#     while(True):
#         dado = p.topo()
#         print(dado)
#         carga = p.desempilha()
#         print(f'{carga}\n')
# except PilhaException as pe:
#     print(pe)