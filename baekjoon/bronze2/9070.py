import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    kind = int(input())
    price_per_gram = []
    for j in range(kind):
        w, c = map(int, input().split())
        price_per_gram.append((c/w, c))
    price_per_gram.sort(key=lambda x: (x[0],x[1]))
    print(price_per_gram[0][1])

