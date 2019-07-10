import numpy

dimension = list(map(int, input().split()))
n = dimension[0]
m = dimension[1]

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr)

print(numpy.transpose(arr))
print(arr.flatten())
