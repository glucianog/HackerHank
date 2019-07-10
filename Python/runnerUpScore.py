if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    winner = -100
    runnerup = -100

    p = [x for x in arr]

    for x in p:
        winner = x if x >= winner else winner

    p = [value for value in p if value != winner]

    for x in p:
        runnerup = x if x > runnerup else runnerup

    print(runnerup)
    
