from collections import Counter

def earnedAmount(availableSizes, n):
    result = 0
    for _ in range(n):
        size, price = input().split()
        if Counter(availableSizes)[int(size)] != 0:
            result += int(price)
            availableSizes.remove(int(size))    
    return result



if __name__ == "__main__":
    x = int(input())
    availableSizes = list(map(int, input().split()))
    n = int(input())   

    print(earnedAmount(availableSizes, n))

