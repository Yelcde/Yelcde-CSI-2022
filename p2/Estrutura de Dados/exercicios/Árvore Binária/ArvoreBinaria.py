class No:
    def __init__(self,carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None

    def __str__(self):
        return str(self.carga)


class ArvoreBinaria:        
    def __init__(self, carga_da_raiz:any = None):
        if carga_da_raiz is None:
            self.__raiz = carga_da_raiz
        else:
            self.__raiz = No(carga_da_raiz)
        self.__cursor = self.__raiz
        self.__tamanho = 0

    def estaVazia(self)->bool:
        return self.__raiz == None
    
    def criaRaiz(self, carga:any):
        if self.__raiz is None:
            self.__raiz = No(carga)
            self.__tamanho += 1

    def getRaiz(self)->any:
        return self.__raiz.carga if self.__raiz is not None else None

    def getCursor(self)->any:
        return self.__cursor.carga if self.__cursor is not None else None

    def preordem(self):
        self.__preordem(self.__raiz)

    def __preordem(self, no:No):
        if no is not None:
            print(f'{no.carga}',end=' ')
            self.__preordem(no.esq)
            self.__preordem(no.dir)

    def emordem(self):
        self.__emordem(self.__raiz)

    def __emordem(self, no):
        if no is not None:
            self.__emordem(no.esq)
            print(f'{no.carga}',end=' ')
            self.__emordem(no.dir)

    def posordem(self):
        self.__posordem(self.__raiz)

    def __posordem(self, no):
        if no is not None:
            self.__posordem(no.esq)
            self.__posordem(no.dir)
            print(f'{no.carga}',end=' ')

    def descerEsquerda(self):
        if self.__cursor is not None and self.__cursor.esq is not None:
            self.__cursor = self.__cursor.esq

    def descerDireita(self):
        if self.__cursor is not None and self.__cursor.dir is not None:
            self.__cursor = self.__cursor.dir

    def resetCursor(self):
        self.__cursor = self.__raiz

    def addEsq(self, carga:any)->bool:
        if self.__cursor is not None and self.__cursor.esq is None:
            self.__cursor.esq = No(carga)
            self.__tamanho += 1
            return True
        else:
            return False
    
    def addDir(self, carga)->bool:
        if  self.__cursor.dir is None:
            self.__cursor.dir = No(carga)
            self.__tamanho += 1
            return True
        else:
            return False

    def __len__(self):
        return self.__tamanho

    def busca(self, chave:any):
        return self.__busca(chave, self.__raiz)
    
    def __busca(self, chave:any, no:No):
        if no is None:
            return False
        if chave == no.carga:
            return True
        if self.__busca(chave,no.esq):
            return True
        else:
            return self.__busca(chave,no.dir)
        
    # Função que conta a altura da Árvore
    def altura(self) -> int:
        return self.__altura_recursive(self.__cursor)

    def __altura_recursive(self, node: No, cursor: No = None) -> int:
        if node is None:
            return 0
        
        count_esq = 0
        count_dir = 0
        
        if node.esq is not None:
            cursor = node
            self.descerEsquerda()
            count_esq += 1 + self.__altura_recursive(self.__cursor, cursor)
            self.__cursor = cursor
        
        if node.dir is not None:
            cursor = node
            self.descerDireita()
            count_dir += 1 + self.__altura_recursive(self.__cursor, cursor)
            self.__cursor = cursor
        
        return max(count_dir, count_esq)
    
    # Método que conta a quantidade de nós na Árvore
    def count(self):
        return self.__count(self.__raiz)
    
    def __count(self, no):
        if no is None:
            return 0 
        
        quantno = 1

        quantno += self.__count(no.esq)
        quantno += self.__count(no.dir)

        return quantno
        
    def go(self, chave:int ):
        pass
    
    def __go(self, chave:int, node:No)->No:
        pass