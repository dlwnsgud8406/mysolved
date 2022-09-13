def combination(a, b):
    up = 1
    down = 1
    anchor = b
    for i in range(0, anchor):
        up = up * a
        a = a - 1
    for j in range(0, b):
        down = down * anchor
        anchor = anchor - 1
    result = up // down
    return result

T = input()
T = int(T)
answer = []
for i in range(0, T):
    N, M = input().split()
    N = int(N)
    M = int(M)
    answer.append(combination(M,N))

for j in range(0, T):
    print(answer[j])
