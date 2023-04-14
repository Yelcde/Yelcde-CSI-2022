class PilhaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        

class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__prox = None

    
    def getCarga(self):
        return self.__carga

    def getProximo(self)->'No':
        return self.__prox
    
    def setProximo(self, novoProx:'No'):
        self.__prox = novoProx

    def temProximo(self)->bool:
        return self.__prox == None

    def __str__(self):
        return f'{self.__carga}'


class Pilha:

    def __init__(self):
        self.__topo = None  
        self.__tam = 0

        
    def estaVazia(self)->bool:
        return self.__topo == None


    def __len__(self):
        return self.__tam


    def tamanho(self)->int:
        return self.__tam
        

    def elemento(self, posicao:int)->any:
        if self.__topo is None:
            raise PilhaException("A pilha está vazia! Adicione itens")
        if (self.__topo is None) and (posicao > self.__tam) or (posicao < 0):
            raise PilhaException(f'Me dê uma posição válida! Entre 1 e {self.__tam}')
            
        pos = 1
        cursor = self.__topo
        while (pos <= self.__tam):            
            if (pos == posicao):
                return f'Na posicao {posicao} está o item {cursor.getCarga()}'
            pos += 1
            cursor = cursor.getProximo()

        return PilhaException(f'O item {posicao} não existe na pilha')

                
    def busca(self, key:any)->int:
        if self.__topo is None:
            raise PilhaException("Não há itens para buscar! Adicione itens")

        pos = 1
        cursor = self.__topo
        while (pos <= self.__tam):            
            if (cursor.getCarga() == key):
                return f'A posição do item {key} é {pos}'
            pos += 1
            cursor = cursor.getProximo()

        raise PilhaException(f'O item {key} não existe na pilha')


    def topo(self)->any:
        if self.__tam == 0:
            return PilhaException('Não há topo, a pilha está vazia')
        return f'Esse é o topo da pilha: {self.__topo}'


    def empilha(self, carga:any):
        no = No(carga)
        no.setProximo(self.__topo)
        self.__topo = no
        self.__tam += 1


    def desempilha(self)->any:
        if self.__topo is None:
            raise PilhaException('Não há elementos para remoção. Pilha Vazia')
        carga = self.__topo.getCarga()
        self.__topo = self.__topo.getProximo()
        self.__tam -= 1
        return f'O item {carga} foi removido!'

        
    def __str__(self)->str:
        s = 'topo->[ '
        cursor = self.__topo
        while(cursor != None):
            s += f'{cursor.getCarga()} '
            if cursor.getProximo() is not None:
                s+= ', '
            cursor = cursor.getProximo()
        # s = 
        # s += ' ]'
        # return s[:-2] + ' ]'
        return s + "]"