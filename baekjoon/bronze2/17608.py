import sys
input = sys.stdin.readline
n = int(input())
answer = 0
high_max = 0
arr = []
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    if high_max < arr[n-1-i]:
        high_max = arr[n-1-i]
        answer += 1
print(answer)
