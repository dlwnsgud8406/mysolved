import sys
input = sys.stdin.readline
cost = 10001
answer = 0
n = int(input())
arr = []
for i in range(n):
    d, c = map(int, input().split())
    arr.append((d, c))
arr.sort()
for condo in arr:
    temp = condo[1]
    if temp < cost:
        cost = temp
        answer += 1
print(answer)
