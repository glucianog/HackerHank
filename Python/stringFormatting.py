def print_formatted(number):
    spaces = len(bin(number)[2:])

    for i in range(number):
        string = insertSpaces(spaces - len(str(i+1)))
        string += str(i+1)
        string += insertSpaces(spaces + 1 - len(oct(i+1)[2:]))        
        string += oct(i+1)[2:]
        string += insertSpaces(spaces + 1 - len(hex(i+1)[2:]))  
        string += str(hex(i+1)[2:]).upper()
        string += insertSpaces(spaces + 1 - len(bin(i+1)[2:]))  
        string += bin(i+1)[2:]
        print(string)

def insertSpaces(value):
    string = ""
    for _ in range(value):
        string += " "
    return string

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)