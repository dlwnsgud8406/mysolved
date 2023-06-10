from math import factorial
T = int(input())
for i in range(T):
    n = int(input())
    fac = str(factorial(n))
    for j in range(len(fac)):
        if fac[len(fac) -(j + 1)] != '0':
            print(fac[len(fac) -(j + 1)])
            break
