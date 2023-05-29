n = int(input())
n -= 1
count = 3
for i in range(0, n):
    if i**2 + i == n:
        print(i)
