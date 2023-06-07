import math

def prime_number(x):
    for in_i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % in_i == 0:
            return 0
    return x  # 소수임

prime = []
a = int(input())
b = int(input())
for i in range(a, b + 1):
    receive = prime_number(i)
    if receive > 1:
        prime.append(receive)


if len(prime) < 1:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))


