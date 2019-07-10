import textwrap

def merge_the_tools(string, k):    
    substrings = textwrap.wrap(string, k)
    for sequence in substrings:
        result = ""
        for c in sequence:
            if c not in result:
                result += c
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)