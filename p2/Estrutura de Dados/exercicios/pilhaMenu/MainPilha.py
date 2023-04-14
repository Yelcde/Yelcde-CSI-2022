from PilhaEncadeada import Pilha, PilhaException

p = Pilha()

for i in range (1,11):
    p.empilha(i*10)

print(f'{p}\n')
try:
    busca = p.busca(22)
    print(f'{busca}\n')
except PilhaException as pe:
    print(pe, '\n')
    
elemento = p.elemento(12)
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