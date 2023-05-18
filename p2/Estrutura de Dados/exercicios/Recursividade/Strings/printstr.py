def printstr(string):
    if len(string) == 0:
        return
    printstr(string[:-1])
    print(string[-1], end='')

if __name__ == "__main__":
    printstr('Johnner')