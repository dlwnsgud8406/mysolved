n, m = map(int, input().split())
arr = list(range(0, m, 1))
arr_1 = []
for i in range(n):
    arr_1.append(input())
input()
arr_2 = []
for i in range(n):
    arr_2.append(input())
count = 0
for a, b in zip(arr_1, arr_2):
    for i in range(m):
        if a[i] == b[i]:
            count += 1
print(count)
