def swap_case(s):
    result = ''

    for i in s:
        result += (i.lower() if i.isupper() else i.upper())

    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)