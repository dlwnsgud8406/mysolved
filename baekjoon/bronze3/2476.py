n = int(input())
arr = []
for i in range(n):
    a, b, c = sorted(map(int, input().split()))
    if a==b==c:
        arr.append(10000+(a * 1000))
    elif a==b:
        arr.append(1000+(100*a))
    elif b==c:
        arr.append(1000 + (100 * b))
    elif c==a:
        arr.append(1000 + (100 * c))
    else:
        arr.append(c*100)
print(max(sorted(arr)))
