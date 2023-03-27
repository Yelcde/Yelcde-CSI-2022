from PilhaEncadeada import Pilha, PilhaException

# Criando instancia
p = Pilha()

# Gerando os itens da Pilha
for i in range (1,11):
    p.empilha(i*10)

try:
    # Buscando por posição
    print(p.elemento(1))

    # Buscando por Carga
    print(p.busca(10))

    print(p)
    print(len(p))

    # Desempilhando
    while(True):
        print('desempilha: ', p.desempilha())
    print(p)
    print(len(p))
except PilhaException as pe:
    print(pe)