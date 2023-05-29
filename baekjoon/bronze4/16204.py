n, m, k = map(int, input().split())
a = min(m, k)
b = min((n-m), (n-k))

print(a + b)
