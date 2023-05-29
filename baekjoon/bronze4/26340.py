n = int(input())
for i in range(1, n + 1):
    # read input
    a, b, f = map(int, input().split())
    print("Data set: %d %d %d"%(a, b, f))
    # apply folds
    for j in range(f):
        if a > b:
            a //= 2
        else:
            b //= 2

    # print output

    print("%d %d\n"%(max(a,b), (min(a, b))))
