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
        """ Método que recupera a carga armazenada em um determinado elemento da pilha

        Args:
            posicao (int): um número correpondente à ordem do elemento existente.
                           Sentido: da base em direção ao topo
        
        Returns:
            Any: a carga armazenada no elemento correspondente à posição indicada.

        Raises:
            PilhaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a uma posição  que excede a
                      quantidade de elementos da lista.                      
        Examples:
            p = Pilha()
            ...   # considere que temos internamente a pilha [10,20,30,40]<-topo
            posicao = 5
            print (p.elemento(3)) # exibe 30
        """
        pass
                
    def busca(self, key:any)->int:
        """ Método que retorna a posicao ordenada, dentro da pilha, em que se
            encontra uma chave passado como argumento. No caso de haver mais de uma
            ocorrência do valor, a primeira ocorrência será retornada.
            O ordenamento que determina a posição é da base para o topo.

        Args:
            key (any): um item de dado que deseja procurar na pilha
        
        Returns:
            int: um número inteiro representando a posição, na pilha, em que foi
                 encontrada a chave.

        Raises:
            PilhaException: Exceção lançada quando o argumento "key"
                  não está presente na pilha.

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]<-topo
            print (p.elemento(40)) # exibe 4
        """
        pass

    def topo(self)->any:
        """ Método que devolve o elemento localizado no topo, sem desempilhá-lo.
    
        Returns:
            any: o conteúdo armazenado no elemento do topo

        Raises:
            PilhaException: Exceção lançada quando se tenta consultar o topo de uma
                   uma pilha vazia
                    
        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]
            dado = p.topo()
            print(dado) # exibe 40
        """
        if self.__tam == 0:
          raise PilhaException('Não há elementos para remoção. Pilha Vazia')
          # raise PilhaException('Não há topo, a pilha está vazia')
        return self.__topo

    def empilha(self, carga:any):
        """ Método que adiciona um novo elemento ao topo da pilha

        Args:
            carga (any): a carga que será armazenada no novo elemento do topo da pilha.

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]
            p.empilha(50)
            print(p)  # exibe [10,20,30,40,50]
        """
        no = No(carga)
        no.setProximo(self.__topo)
        self.__topo = no
        self.__tam += 1


    def desempilha(self)->any:
        """ Método que remove um elemento do topo da pilha e retorna
            sua carga correspondente.
    
        Returns:
           any: a carga armazenada no elemento removido

        Raises:
            PilhaException: Exceção lançada quando se tenta remover algo de uma pilha vazia
                    
        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]
            dado = p.desemplha()
            print(p) # exibe [10,20,30]
            print(dado) # exibe 40
        """
        if self.__topo is None:
            raise PilhaException('Não há elementos para remoção. Pilha Vazia')
        carga = self.__topo.getCarga()
        self.__topo = self.__topo.getProximo()
        self.__tam -= 1
        return carga
   
    def imprime(self):
        """ Método que exibe na tela a sequência ordenada dos elementos da pilha

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a pilha [10,20,30,40]<-topo
            p.imprimir()) # exibe Lista: [10,20,30,40] <- topo
        """  
        pass
        
    def __str__(self)->str:
        """ Método que retorna a ordenação atual dos elementos da pilha, do
            topo em direção à base

        Returns:
           str: a carga dos elementos da pilha, do topo até a base
        """  
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

 

