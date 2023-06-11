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
arv.descerDireita()
arv.addDir(8)

arv.resetCursor()

arv.preordem()

tamanhoArv = arv.altura()
print(f'\nO tamanho da arvore é: {tamanhoArv}')

quantno = arv.count()
print(f'A quantidade de nós na arvore é: {quantno}')

folhas = arv.leafs()
print(f'A quantidade de folhas na arvore é: {folhas}')

getLevel = arv.getLevel(8)
print(f'O nível referente a esse item na arvore é: {getLevel}')