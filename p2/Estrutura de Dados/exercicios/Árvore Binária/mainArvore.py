from ArvoreBinaria import ArvoreBinaria

# Instamciando Arvore
arv = ArvoreBinaria(1)

# Adicionando nó esquerdo
arv.addEsq(2)
# Adicionando nó direito
arv.addDir(3)
# Descendo um nó a esquerda do curso
arv.descerEsquerda()
print('Cursor: ', arv.getCursor())
# Adicionando nó a direita do nó 2
arv.addDir(4)
# Resetando cursor
arv.resetCursor()
# Descendo pro nó a direita da raiz
arv.descerDireita()
# Adicionando nó a esquerda e a direita no nó 3
arv.addEsq(5)
arv.addDir(6)
arv.descerDireita()
arv.addDir(7)

arv.resetCursor()

arv.preordem()

tamanhoArv = arv.count()
print(f'\nO tamanho da arvore é: {tamanhoArv}')


# arv.addEsq(10)
# arv.addDir(20)
# arv.resetCursor()
# arv.descerDireita()
# print('Cursor: ', arv.getCursor())
# arv.addDir(55)
# arv.descerDireita()
# print('Cursor: ', arv.getCursor())
# arv.addEsq(8)
# 
# print('Busca:', arv.busca(578))
# 
# arv.preordem()
# print()
# arv.emordem()
# print()
# arv.posordem()