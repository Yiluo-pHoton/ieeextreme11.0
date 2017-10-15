import math

def getAllPrimes(n, d):
    array = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n) + 1)):
        if array[i]:
            for j in range(i**2, n + 1, i):
                array[j] = False
    counter = 0
    for i in range(2, n + 1):
        if array[i] and i != d:
            counter += 1
    return counter

t, a, b = [int(i) for i in input().split()]
for i in range(t):
    d = int(input())
    for i in range(a, b):
        getAllPrime(i, d)
