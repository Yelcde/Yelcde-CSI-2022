class Carta:

    def __init__(self, numero:str, naipe:str, pontuacao:int=0):
        # Definindo as propriedades

        self.naipe = naipe
        self.numero = numero
        self.pontuacao = pontuacao


    def getNaipe(self)->str:
        return self.naipe

    def getNumero(self)->str:
        return self.numero

    def getPontuacao(self)->int:
        return self.pontuacao

    def setPontuacao(self, novaPontuacao:int):
        self.pontuacao = novaPontuacao

    def __str__(self):
        return f'{self.numero} de {self.naipe}: {self.pontuacao}'