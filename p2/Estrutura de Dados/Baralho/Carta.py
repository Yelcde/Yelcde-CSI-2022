class Carta:

    def __init__(self, numero:str, naipe:str):
        # Definindo as propriedades

        self.naipe = naipe
        self.numero = numero
        self.pontuação = 0


    def getNaipe(self):
        pass

    def getNumero(self):
        pass

    def getPontuacao(self):
        pass

    def setPontuacao(self):
        pass

    def __str__(self):
        return f'{self.numero} de {self.naipe}'