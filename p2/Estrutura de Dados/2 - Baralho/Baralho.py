from Carta import Carta
import random 

class Baralho:

    # Criando o Baralho
    def __init__(self):
        self.__cartas = []
        naipe = ["Copas", 'Ouro', "Paus", "Espedas"]
        numero = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]

        for np in naipe:
            for num in numero:
                self.__cartas.append(Carta(num, np))

    # Tamanho do Baralho
    def __len__(self):
        return len(self.__cartas)

    # Texto
    def __str__(self):
        s = ''
        contador = 0
        for carta in self.__cartas:
            s += carta.__str__() + '\t'
            contador += 1
        if ((contador % 3) == 0):
            s += '\n'
        return s

    # Embaralhar
    def embaralhar(self):
        random.shuffle(self.__cartas) # Embaralhar os itens

    # Retirar cartas
    def retiraCartas(self) ->Carta:
        return self.__cartas.pop()

    # Testando se a carta ta no Baralho
    def __cartaEstaNoBaralho(self, carta:Carta):
        if not self.__cartaEstaNoBaralho(carta):
            return carta in self.__cartas

    # Repondo Cartas
    def reporCarta(self, carta:Carta):
        self.__cartas.insert(0, carta)