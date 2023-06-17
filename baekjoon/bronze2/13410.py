a, b = map(int, input().split())
arr = []
reverse_arr = []
for i in range(1, b+1):
    arr.append(a * i)
arr = list(map(str, arr))
for char in arr:
    reverse_arr.append(char[::-1])

print(max(list(map(int, reverse_arr))))
