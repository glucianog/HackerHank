def writeDashes(n):
    result = ""
    for _ in range(n):
        result+= "-"
    return result

def writeLetters(n, lastLetter):
    result = ""
    aux = 0
    for x in range(n):
        result += chr(lastLetter - x)
        if x < n-1:
            result += "-"
        aux = lastLetter - x
    for x in range(1,n):        
        result += "-"
        result += chr(aux+x)

    return result

def rangoli(n, lastLetter):
    for i in range(1,n):
        string = writeDashes(2*n - 2*i) #left dashes
        string += writeLetters(i, lastLetter)#letters
        string += writeDashes(2*n - 2*i) #right dashes
        print(string)
    print(writeLetters(n, lastLetter))

    for i in range(n-1,0,-1):
        string = writeDashes(2*n - 2*i) #left dashes
        string += writeLetters(i, lastLetter)#letters
        string += writeDashes(2*n - 2*i) #right dashes
        print(string)


if __name__ == '__main__':
    n = int(input())
    lastLetter = 96 + n
    rangoli(n, lastLetter)