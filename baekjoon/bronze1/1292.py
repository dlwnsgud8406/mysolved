import sys
input = sys.stdin.readline
a, b = map(int, input().split())
arr = []
answer = 0
for i in range(46):
    for j in range(i):
        arr.append(i)
for i in range(a-1, b):
    answer += arr[i]
print(answer)
