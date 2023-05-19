def compareStr(str1, str2):
    global i
    global j
    if len(str1) == 0 and len(str2) == 0:
        return 
    if len(str1) > 0: 
        i += 1
        compareStr(str1[1:], str2)
    else:
        j += 1
        compareStr(str1, str2[1:])
    return i and j


if __name__ == "__main__":
    global i 
    i = 0
    global j
    j = 0
    compareStr('Jyan', "Sammuel")
    if i == j:
        print('str1 é igual a str2')
    elif i > j:
        print('str1 é maior a str2')
    elif i < j:
        print('str1 é menor a str2')