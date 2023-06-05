def bubleSort(lista):
    if len(lista) == 1:
        return
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            var = lista[i+1]
            lista[i+1] = lista[i]
            lista[i] = var
            print(lista)
    return bubleSort(lista[0:-1])

if __name__ == '__main__':
    lista = [25, 48, 37, 12, 57, 86, 33, 92]
    bubleSort(lista)
    print(lista)