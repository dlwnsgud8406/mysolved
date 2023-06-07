n = int(input())
if n == 0:
    print(0)
if n == 1:
    print(1)
else:
    answer = 1
    a = 0
    b = 0
    for i in range(n - 1):
        a = answer
        answer = a + b
        b = a
    print(answer)

