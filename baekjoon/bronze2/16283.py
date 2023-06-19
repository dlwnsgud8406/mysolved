a, b, n, w = map(int, input().split())
arr = []
for sheep in range(1, n):
    goat = n - sheep
    if sheep * a + goat * b == w:
        arr.append((sheep, goat))
if len(arr) >= 2 or len(arr) == 0:
    print(-1)
else:
    print(arr[0][0], arr[0][1])
