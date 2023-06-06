n = int(input())
a = 3
b = 2
c = 2
answer = 12
if n == 1:
    print(5)
else:
    for i in range(2, n):
        a += 1
        b += 1
        c += 1
        answer += (a+b+c)
    print(answer % 45678)
