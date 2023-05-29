n, m = map(int, input().split())
arr = [0] * n
for i in range(m):
    a, b, c = map(int, input().split())
    for j in range(0, b + 1 - a):
        arr[a + j - 1] = c
for num in arr:
    print(num, end=' ')

