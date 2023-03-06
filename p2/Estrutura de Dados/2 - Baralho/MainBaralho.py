from Carta import Carta
from Baralho import Baralho

c1 = Carta('Valete', 'Espada')
print(id(c1))
print(c1.getNaipe())
print(c1.getPontuacao())
c1.setPontuacao(10)
print(c1.getPontuacao())
print(c1)

print(c1.__str__())

c2 = Carta('Dama', 'Ouro')
c3 = Carta('As', 'Paus', 5)
print(c2)
print(c3)

b1 = Baralho()
# print(b1)
# print(len(b1))
b1.embaralhar()
print(b1)

for i in range(10):
    b1.retiraCartas()

cartaRetirada = b1.retiraCartas()
print('\nCarta Retirada', cartaRetirada)
# print(len(b1))
b1.reporCarta(cartaRetirada)
print(len(b1))
print(b1)