class FilaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)


class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__prox = None

    @property
    def carga(self):
        return self.__carga
    
    @carga.setter
    def carga(self, novaCarga):
        self.__carga = novaCarga

    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, novoNo):
        self.__prox = novoNo   

    def temProximo(self)->bool:
        return self.__prox == None

    def __str__(self):
        return f'{self.__carga}'

class Head:
    def __init__(self):
        self.__frente = None
        self.__final  = None
        self.__tam = 0
    
    @property
    def frente(self):
        return self.__frente
    
    @property
    def final(self):
        return self.__final

    @property
    def tam(self):
        return self.__tam

    @frente.setter
    def frente(self, novoNo):
        self.__frente = novoNo
    
    @final.setter
    def final(self, novoNo):
        self.__final = novoNo

    @tam.setter
    def tam(self, novoNo):
        self.__tam = novoNo


class Fila:

    def __init__(self):
        self.__head = Head()

    
    def estaVazia(self)->bool:
        return self.__head.tam == 0

    def __len__(self)->int:
        return self.__head.tam

    def enfileira(self, carga:any):
        novoNo = No(carga)
        if self.estaVazia():
            self.__head.frente = self.__head.final = novoNo
        else:
            self.__head.final.prox = novoNo
            self.__head.final = novoNo
        self.__head.tam += 1

    def modificaValor(self, posicao, novoValor):
        try:
            if posicao <= 0 or posicao > self.__len__():
                return FilaException(f"Posicao invalida. A fila só tem {self.__len__()} elementos.\n")
        except:
            return FilaException(f'Digite um número entre 1 e {self.__len__()}\n')
        
        contador = 1
        cursor = self.__head.frente
        while(cursor != None):
            if contador == posicao:
                self.__head.final.prox = novoValor
                self.__head.final = novoValor
            cursor = cursor.prox
            contador += 1        

    
    def desenfileira(self, posicao)->any:
        if self.estaVazia():
            return FilaException("A fila está vazia")
        try:
            if posicao <= 0 or posicao > self.__len__():
                return FilaException(f"Posicao invalida. A fila só tem {self.__len__()} elementos.\n")
        except:
            return FilaException(f'Digite um número entre 1 e {self.__len__()}\n')
        
        contador = 1
        cursor = self.__head.frente
        while(cursor != None):
            carga = self.__head.frente.carga
            if self.__head.tam == 1:
                self.__head.final = None
            if contador == posicao:
                self.__head.frente = self.__head.frente.prox
                self.__head.tam -= 1
                cursor = cursor.prox
                contador += 1    
                return carga
                

    def elemento(self, posicao:int)->any:
        try:
            if posicao <= 0 or posicao > self.__len__():
                return FilaException(f"Posicao invalida. A fila só tem {self.__len__()} elementos.\n")
        except:
            return FilaException(f'Digite um número entre 1 e {self.__len__()}\n')
        
        contador = 1
        cursor = self.__head.frente
        while(cursor != None):
            if contador == posicao:
                return f'A posição {posicao} é correspondente ao valor {cursor.carga}'
            cursor = cursor.prox
            contador += 1        
                
    def busca(self, key:any)->int:
        contador = 1
        cursor = self.__head.frente
        while(cursor != None):
            if key == cursor.carga:
                return f'A chave {key} é correspondente a posição {contador}\n'
            cursor = cursor.prox
            contador += 1

        return FilaException(f"A chave {key} não está na fila.")

    def __str__(self)->str:
        s = 'frente-> [ '
        cursor = self.__head.frente
        while(cursor != None):
            s += f'{cursor.carga}, ' 
            cursor = cursor.prox
        if self.estaVazia():
            return s + ' ]'
        return s[:-2] + ' ]'