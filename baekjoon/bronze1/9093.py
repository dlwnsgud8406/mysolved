n = int(input())
for i in range(n):
    arr = input().split()
    for char in arr:
        print(char[::-1], end=' ')
    print()
