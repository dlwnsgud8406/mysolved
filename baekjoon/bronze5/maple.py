a, b = map(int, input().split())
b = 100 - b
b /= 100

if a*b >= 100:
    print(0)
else:
    print(1)
