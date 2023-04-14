class FilaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)
    


class Fila:
    def __init__(self, capacidade: int = 10):
        if capacidade <= 0:
            raise FilaException("A fila deve ser criada com um valor maior do que zero")
        self.__capacidade = capacidade # Tamanho máximo da ficha
        self.__inicio = 0 # Indice do primeiro elemento
        self.__fim = -1 # Indice do último elemento da fila
        self.__fila = [None] * capacidade
        self.__ocupados = 0
    
        
    def estaVazia(self)->bool:
        return self.__ocupados == 0


    def estaCheia(self)->bool:
        return self.__ocupados == self.__capacidade


    def __len__(self):
        return self.__ocupados

    def getCapacidade(self)->int:
        return self.__capacidade


    def tamanho(self)->int:
        pass


    def elemento(self, posicao:int)->any:
        if posicao <= 0 or posicao > self.__len__():
            raise FilaException(f"Posição Inválida! A Fila só tem {self.__len__()}")
        
        return self.__fila[(self.__inicio + (posicao - 1)) % self.__capacidade]
        
                
    def busca(self, key:any)->int:
        index = self.__inicio
        for i in range(self.__ocupados):
            if key == self.__fila[index]:
                return i+1
            index = (index + 1) % self.__capacidade


    def topo(self)->any:
        pass


    def enfileira(self, carga:any):
        if self.estaCheia():
           raise FilaException("A Fila está cheia")

        self.__fim = (self.__fim + 1) % self.__capacidade
        self.__fila[self.__fim] = carga
        self.__ocupados += 1


    def desenfileira(self)->any:
        if self.estaVazia():
            raise FilaException("A Fila está vazia")
        
        carga = self.__fila[self.__inicio]
        self.__inicio = (self.__inicio + 1) % self.__capacidade
        self.__ocupados -= 1
        return carga

        
    def __str__(self)->str:
        s = 'frente->[ '
        index = self.__inicio
        for i in range(self.__ocupados):
            s += f'{self.__fila[index]}, '
            index = (index + 1) % self.__capacidade
            
        return s[:-2] + "]"   