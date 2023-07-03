class TabelaHash:
    def __init__(self, max):
        self.__table = [None for i in range(max)]
        self.__capacidade = max
        self.__ocupados = 0
        self.__numPrimo = self.__numPrimo(self.__capacidade)
    
    def __numPrimo(self, capacidade):
        sub = 1
        while capacidade != 0:
            capacidade = capacidade - sub
            if (capacidade % 2) != 0:
                return capacidade

    def __len__(self):
        return self.__ocupados

    def put(self, key:any, value:any):
        if self.__ocupados < self.__capacidade:
            slot = self.__hash(key)
            if (self.__table[slot] is None):
                self.__table[slot] = value                
            else:  # tratar colisao aqui
                nextSlot = self.__reHash(slot)
                while(self.__table[nextSlot] is not None):
                    nextSlot = self.__espDuplo(slot)
                self.__table[nextSlot] = value
            self.__ocupados += 1

    def get(self, key:any)->any:
        pass

    def __hash(self, key:any):
        return hash(key) % self.__capacidade
    
    # Espelhamento Duplo
    def __reHash(self, key):
        return self.__numPrimo - (key % self.__numPrimo) 
    
    def __espDuplo(self, h1, h2):
        pass

    def __str__(self):
        s = ''
        for i in range(self.__capacidade):
            s += f'{self.__table[i]} '
        return s

# teste
ht = TabelaHash(13)
ht.put(12,12)
ht.put(31,31)
ht.put(90,90)
ht.put(28,28)
ht.put(77,77)
ht.put(26,26)
# ht.put(400,"GBR")
# ht.put(600,"RTG")
# ht.put(700,"ZZZ")
# ht.put(900,"ASW")
# ht.put(358,"ERR")

print(ht)