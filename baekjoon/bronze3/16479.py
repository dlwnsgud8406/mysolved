k = int(input())
d1, d2 = map(int, input().split())
answer = k**2 - (abs(d1-d2)/2)**2
if int(answer) == k**2 - (abs(d1-d2)/2)**2:
    print(int(answer))
else:
    print(answer)

