import numpy

arr = map(int, input().split())

myarr = [p for p in arr]

print(numpy.reshape(myarr, (3,3)))

