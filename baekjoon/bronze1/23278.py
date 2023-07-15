import sys
input = sys.stdin.readline
n, l, h = map(int, input().split())
arr = sorted(map(int, input().split()))
for i in range(l):
    del(arr[0])
for i in range(h):
    del(arr[len(arr)-1])
print((sum(arr) / (n-l-h)))

