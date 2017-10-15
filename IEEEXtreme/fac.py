import math

def facFromTo(b, c):
    prod = 1
    for i in range(b, c, -1):
        prod *= i
    return prod

def fac(a):
    prod = 1
    for i in range(1, a + 1):
        prod *= i
    return prod

def power(base, exp):
   if exp == 0:
      return 1
   elif exp == 1:
      return base
   elif (exp & 1) != 0:
       return base * power(base * base, exp // 2)
   else:
       return power(base * base, exp // 2)

n = int(input())
for i in range(n):
    a, b, c = [int(i) for i in input().split()]
    print(a, b, c)
    if a == 1:
        print(1)
    else:
        print(facFromTo(b, c)/fac(b-c))
        print(power(a, int(facFromTo(b, c)/fac(b-c))) % (power(10, 9)+7))
