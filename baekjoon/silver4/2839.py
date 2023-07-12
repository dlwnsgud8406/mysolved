n = int(input())
if n == 4 or n == 7:
    print(-1)
else:
    print(n // 5 + n % 5 - 2 * ((n % 5) // 3))
