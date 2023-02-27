from Carta import Carta
import random 

class Baralho:

    # Criando o Baralho
    def __init__(self):
        self.cartas = []
        naipe = ["Copas", 'Ouro', "Paus", "Espedas"]
        numero = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]

        for np in naipe:
            for num in numero:
                self.cartas.append(Carta(num, np))

    # Tamanho do Baralho
    def __len__(self):
        return len(self.cartas)

    # Texto
    def __str__(self):
        s = ''
        contador = 0
        for carta in self.cartas:
            s += carta.__str__() + '\t'
            contador += 1
        if ((contador % 3) == 0):
            s += '\n'
        return s

    # Embaralhar
    def embaralhar(self):
        random.shuffle(self.cartas) # Embaralhar os itens

    # Retirar cartas
    def retiraCartas(self) ->Carta:
        return self.cartas.pop()

    # Repondo Cartas
    def reporCarta(self, carta:Carta):
        self.cartas.insert(0, carta)