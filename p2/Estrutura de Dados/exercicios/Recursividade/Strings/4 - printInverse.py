def printInverse(string):
    if len(string) == 0:
        return
    print(string[-1], end='')
    printInverse(string[:-1])

if __name__ == "__main__":
    printInverse('Johnner')