import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
arr = sorted(arr, key=lambda x:(x[0], x[1]))
for i in range(n):
    print(arr[i][0], arr[i][1])
