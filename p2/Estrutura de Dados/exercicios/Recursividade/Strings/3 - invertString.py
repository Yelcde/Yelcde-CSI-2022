def invertString(string):
    if len(string) == 0:
        return
    print(string[-1], end='')
    invertString(string[:-1])

if __name__ == "__main__":
   invertString('Johnner')