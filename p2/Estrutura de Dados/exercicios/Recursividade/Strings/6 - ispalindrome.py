def ispalindrome(string):
    if len(string) <= 1:
        print('É palindromo')
        return 
    if string[0] == string[-1]:
        ispalindrome(string[1:-1])
    else:
        print('Não É palindromo')
        return 

if __name__ == "__main__":
    ispalindrome('subinosunibus')