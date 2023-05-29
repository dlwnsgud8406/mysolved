n, a, b = map(int, input().split())
arr = []
col = []
a -= 1
b -= 1
for i in range(n):
    arr.append(list(map(int, input().split())))
popularity = arr[a][b]
for i in range(n):
    col.append(arr[i][b])
if max(popularity, max(col), max(arr[a])) == popularity:
    print('HAPPY')
else:
    print('ANGRY')
