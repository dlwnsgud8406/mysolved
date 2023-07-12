T = int(input())
for i in range(T):
    n = int(input())
    whale = sorted(list(input().split()))
    dolphin = sorted(list(input().split()))

    count = 0
    for j in range(n):
        if whale[j] != dolphin[j]:
            print('CHEATER')
            break
        else:
            count += 1
        if count == n:
            print('NOT CHEATER')
