from FilaSequencialCircular import Fila,FilaException

fila = Fila()
fila.enfileira(10)
print(len(fila))
fila.enfileira(20)
print(len(fila))
fila.enfileira(30)
fila.enfileira(40)
print(fila)
print('Elemento(): ', fila.elemento(3))
print('busca(): ', fila.busca(20))

try:
    for i in range(10):
        print(fila.desenfileira())
except FilaException as fe:
    print(fe)

print(fila)
print(len(fila))