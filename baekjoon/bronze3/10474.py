while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    else:
        print("%d %d / %d"%(a//b, a - (a//b) * b, b))
