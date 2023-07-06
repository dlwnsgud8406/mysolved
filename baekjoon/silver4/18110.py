import sys
input = sys.stdin.readline
n = int(input())
if n:
    arr = []
    for i in range(n):
        arr.append(int(input()))
    grade = round((n * 0.15)+0.00000001)
    arr = sorted(arr)[grade:n-grade]
    print(round((sum(arr)/len(arr))+0.00000001))
else:
    print(0)
