n = int(input())
required = 0
for i in range(n):
    g, c, e = map(int, input().split())
    if g == 1:
        print(abs(e-c))
    elif g == 2:
        print(abs(e-c) * 3)
    elif g == 3:
        print(abs(e-c) * 5)
