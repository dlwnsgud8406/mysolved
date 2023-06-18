n, m = map(int, input().split())
case = 1
for i in range(n):
    deck = int(input())
    if deck == 0:
        deck = 1
    case *= deck
print(case % m)

