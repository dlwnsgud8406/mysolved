import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())

# Pre-compute the squares of all possible values
squares = [i*i % 2010 for i in range(2010)]

# Simulate the operations
for i in range(m):
    op, l, r = map(int, input().split())
    if op == 1:
        for j in range(l-1, r):
            a[j] = squares[a[j]]
    elif op == 2:
        print(sum(a[l - 1:r]))


