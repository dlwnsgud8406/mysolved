T = input()
T = int(T)

for i in range(0, T):
    N = input()
    N = int(N)
    if N == 0:
        print("1 0")
    elif N == 1:
        print("0 1")
    else:
        first = 0
        second = 1
        result = 0
        for j in range(0, N):
            first = second
            second = result
            result = first + second
        print(second, result)