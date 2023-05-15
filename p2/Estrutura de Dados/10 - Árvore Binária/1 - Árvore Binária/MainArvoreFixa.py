from No import No

def preordem( no):
    if no is not None:
        print(no.carga)
        preordem(no.esq)
        preordem(no.dir)


def palindrome(str):
    if len(str) == 0:
        return True
    if str[0] == str[-1]:
        return palindrome(str[1:-1])
    else:
        return False

raiz = No(40)
raiz.esq = No(30)
raiz.dir = No(10)



cursor = raiz
cursor = cursor.dir
cursor.dir = No(22)

cursor = cursor.dir 
cursor.esq = No(34)
cursor.dir = No(13)
#raiz.dir.dir = No(22)

preordem(raiz)


print(palindrome('radar'))
exit()