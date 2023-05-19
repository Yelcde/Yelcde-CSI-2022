def compareStr(str1, str2):
    
    global j
    if len(str1) == 0 and len(str2) == 0:
        return 
    if len(str1) > 0:
        global i 
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
    compareStr('Johnner', "Jyan")