class Aluno:
    
    def __init__(self, nome:str, idade:int, matricula:str):
        self.n = nome
        self.i = idade
        self.m = matricula
        
a = Aluno('Johnner Yelcde', 19, "20222370015")

print('Seu nome é:',a.n)
print('Sua idade é:',a.i)
print('Sua matricula é:',a.m)