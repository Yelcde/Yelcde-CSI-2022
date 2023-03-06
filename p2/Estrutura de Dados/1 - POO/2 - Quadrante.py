class Ponto:
    
    def __init__(self, x, y):
        self.linha_x = x
        self.linha_y = y
        
    def quadrante(self):
        if (self.linha_x > 0 and self.linha_y > 0):
            return 'Quadrante 1'
        elif (self.linha_x < 0 and self.linha_y > 0):
            return 'Quadrante 2'
        elif (self.linha_x < 0 and self.linha_y < 0):
            return 'Quadrante 3'
        elif (self.linha_x > 0 and self.linha_y < 0):
            return 'Quadrante 4'
        else:
            return 'Não faz parte de nenhum quadrante'
            
ponto_x = int(input('Me diga o número na linha x: '))
ponto_y = int(input('Me diga o número na linha y: '))
quadrante = Ponto(ponto_x, ponto_y)
print(quadrante.quadrante())