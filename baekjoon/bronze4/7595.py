while 1:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        print('*', end='')
        for j in range(n-i, n):
            print('*', end='')
        print('')
