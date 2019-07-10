from itertools import permutations

def permuteElements(listOfEelements):
    result = []
    for item in aux:
        string = ""
        for c in item:
            string += "".join(c)
        result.append(string)
    return result

if __name__ == "__main__":
    string, k = input().split()
    aux = list(permutations(string, int(k)))
    aux = permuteElements(aux)
    aux.sort()

    for item in aux:
        print(item)