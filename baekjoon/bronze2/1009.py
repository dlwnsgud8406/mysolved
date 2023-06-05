def my_pow(a, b):
    if a == 1 or a == -1 or b == 0:
        return 1
    if a >= 6:
        a %= -10
    if b % 2:
        return a * my_pow(a**2, b // 2)
    else:
        return my_pow(a**2, b // 2)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    num = (my_pow(a, b)) % 10
    if num == 0:
        num = 10
    print(num)
