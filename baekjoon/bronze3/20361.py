import sys

input = sys.stdin.readline

n, x, k = map(int, input().split())
arr = [0] * n
arr[x-1] = 1
for i in range(k):
    a, b = map(int, input().split())
    temp = arr[b-1]
    arr[b-1] = arr[a-1]
    arr[a-1] = temp
print(arr.index(1) + 1)
