from itertools import product


if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    resultlist = list(product(A,B))

    for item in resultlist:
        print(item, end=' ')