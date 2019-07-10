def split_and_join(line):
    phrase = line.split(" ")
    phrase = "-".join(phrase)
    return phrase

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)