def count_substring(string, sub_string):
    value = 0
    begin = 0

    while True:
        begin = string.find(sub_string)
        if begin == -1: break
        value += 1
        string = string[begin+len(sub_string)-1:]

    return value

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)