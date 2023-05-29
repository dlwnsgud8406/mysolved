while 1:

    N, S = map(int, input().split())
    if N > S:
        print('Yes')
    elif N == 0 and S == 0:
        break
    elif N <= S:
        print('No')

