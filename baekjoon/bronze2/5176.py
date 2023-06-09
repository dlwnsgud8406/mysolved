from collections import Counter

T = int(input())
for i in range(T):
    p, m = map(int, input().split())
    arr = []
    for j in range(p):
        arr.append(int(input()))
    dict = Counter(arr)
    print(p - len(dict))

