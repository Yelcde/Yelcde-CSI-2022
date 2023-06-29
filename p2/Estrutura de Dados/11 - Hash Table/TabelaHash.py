class TabelaHash:
    def __init__(self, max):
        self.__table = [None for i in range(max)]
        self.__capacidade = max
        self.__ocupados = 0
    
    def __len__(self):
        return self.__ocupados

    def put(self, key:any, value:any):
        if self.__ocupados < self.__capacidade:
            slot = self.__hash(key)
            if (self.__table[slot] is None):
                self.__table[slot] = value                
            else:  # tratar colisao aqui
                nextSlot = self.__rh(slot)
                while(self.__table[nextSlot] is not None):
                    nextSlot = self.__rh(nextSlot)
                self.__table[nextSlot] = value
            self.__ocupados += 1

    def get(self, key:any)->any:
        pass

    def __hash(self, key:any):
        return hash(key) % self.__capacidade

    def __rh(self, slot):
        return (slot + 1) % self.__capacidade

    def __str__(self):
        s = ''
        for i in range(self.__capacidade):
            s += f'{self.__table[i]} '
        return s

# teste
ht = TabelaHash(10)
print(ht)
print(len(ht))
ht.put(205,"ABC")
ht.put(423,"KLM")
ht.put(500,"BTC")
ht.put(777,"UVW")
ht.put(401,"TYZ")
ht.put(402,"CNN")
print(ht)
ht.put(400,"GBR")
ht.put(600,"RTG")
ht.put(700,"ZZZ")
ht.put(900,"ASW")
ht.put(358,"ERR")


print(ht)
print(len(ht))
