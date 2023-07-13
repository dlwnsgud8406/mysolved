import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
n = int(input())
for _ in range(n):
    a, b = g()
    difference = max(a-b, 1)
    answer = 2 * (a - difference + 1) * (a+difference)
    print(answer)




