# armazenar texto
# contar chars
# armazenamento temporario

from threading import Thread
import time

global texto
texto = ''

global nova_parte
nova_parte = ''

global tamanho_anterior
tamanho_anterior = 0

global salvar_dados
salvar_dados = False

def pegar_texto():
    global texto
    global nova_parte
    while True:
        nova_parte = input()
        texto += nova_parte + ' '

def contar_chars():
    # global texto
    global tamanho_anterior
    global salvar_dados
    while True:
        if (len(texto) > tamanho_anterior):
            print(f'Texto[ {texto} ]')
            print('#chars', len(texto))
            tamanho_anterior = len(texto)
            salvar_dados = True
    time.sleep(0)

def armazenar_temporariamente():
    # global nova_parte
    global salvar_dados
    while True:
        if salvar_dados:
            with open('arq_temp.txt', 'a') as f:
                f.write(nova_parte)
            salvar_dados = False
    time.sleep(0)

t_texto = Thread(target = pegar_texto)
t_texto.start()

t_estatistica = Thread(target = contar_chars)
t_estatistica.start()

t_salvamento = Thread(target = armazenar_temporariamente)
t_salvamento.start()

t_texto.join()
t_estatistica.join()
t_salvamento.join()
print('Main', texto)