class Aluno:
    def __init__(self,matricula,nome):
        self.matricula = matricula
        self.nome = nome
    def __str__(self):
        return f'{self.nome}, matricula {self.matricula}'

    def __eq__(self, other):
        return self.matricula == other.matricula