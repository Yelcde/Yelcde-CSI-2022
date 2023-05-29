def compareStr(str1, str2):
    if len(str1) == 0 and len(str2) == 0:
        print('str1 é igual a str2')
        return
    elif len(str1) == 0:
        print('str1 é menor a str2')
        return
    elif len(str2) == 0:
        print('str1 é maior a str2')
        return
    compareStr(str1[1:], str2[1:])


if __name__ == "__main__":
    compareStr('Jyan', "Sammuel")