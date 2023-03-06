class Retangulo:
    
    def __init__(self, b, a):
        self.altura = a
        self.base = b
        
    def calcArea(self):
        areaRet = self.base * self.altura
        if (self.base == self.altura):
            return f"Isso é um quadrado com base e altura {self.base}x{self.altura} e área {areaRet}"
        else:
            return f"Esse retângulo tem base e altura {self.base}x{self.altura} e área {areaRet}"
    
altura = int(input("Me dê a altura do retângulo: "))
base = int(input("Me dê a base do retângulo: "))
area = Retangulo(altura, base)
print(f'{area.calcArea()}')