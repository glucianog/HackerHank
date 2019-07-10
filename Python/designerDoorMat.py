def writeLine(n, m):
    result = ""
    size = m - (n*3)

    for _ in range(size//2):
        result += "-"

    result += writeSymbols(n)
    
    for _ in range(size//2):
        result += "-"
    
    return result

def writeSymbols(n):
    result = ""
    for _ in range(n):
        result += ".|."
    return result

def writeWelcome(m):
    result = ""
    size = m - 7
    for _ in range(size//2):
        result+= "-"
    result += "WELCOME"
    for _ in range(size//2):
        result+= "-"
    return result


if __name__ == "__main__":
    values = input()
    n, m = values.split(' ')
    nsymbols = 1

    for x in range(int(n)):
        if x < int(n) // 2:
            print(writeLine(nsymbols , int(m)))
            nsymbols += 2
        elif x == int(n)//2:
            print(writeWelcome(int(m)))
        else:  
            nsymbols -= 2          
            print(writeLine(nsymbols, int(m)))
            
