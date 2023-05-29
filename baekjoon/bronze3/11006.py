n = int(input())
for i in range(n):
    n, m = map(int, input().split())
    print("%d %d" % (2 * m - n, n - m))
