def recursiveLength(string):
    if len(string) == 0:
        return 0
    return 1 + recursiveLength(string[1:])

if __name__ == "__main__":
    lenght = recursiveLength('Johnner')
    print(f'O tamanho da frase é {lenght}')