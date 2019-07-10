def hasAlphanumeric(s):
    result = False
    for c in s:
        if c.isalnum(): 
            result = True
    return result

def hasAlphabetical(s):
    result = False
    for c in s:
        if c.isalpha():
            result = True
    return result

def hasDigit(s):
    result = False
    for c in s:
        if c.isdigit():
            result = True
    return result

def hasLowerCase(s):
    result = False
    for c in s:
        if c.islower():
            result = True
    return result

def hasUpperCase(s):
    result = False
    for c in s:
        if c.isupper():
            result = True
    return result

if __name__ == '__main__':
    s = input()

    print(hasAlphanumeric(s))
    print(hasAlphabetical(s))
    print(hasDigit(s))
    print(hasLowerCase(s))
    print(hasUpperCase(s))

