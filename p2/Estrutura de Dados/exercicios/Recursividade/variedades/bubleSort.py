def bubleSort(lista, n):
    if n == 1:
        return
    for i in range(n-1):
        if lista[i] > lista[i+1]:
            var = lista[i+1]
            lista[i+1] = lista[i]
            lista[i] = var
            print(lista)
    return bubleSort(lista, n-1)

if __name__ == '__main__':
    lista = [25, 48, 37, 12, 57, 86, 33, 92]
    bubleSort(lista, len(lista))
    print(lista)