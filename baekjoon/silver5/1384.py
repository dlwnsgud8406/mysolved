import sys
input = sys.stdin.readline
count = 1
while 1:
    n = int(input())
    if n == 0:
        exit(0)
    else:
        print('Group', count)
        message = [input().split() for _ in range(n)]
        flag = True
        for i in range(n):
            for j in range(1, n):
                if message[i][j] == 'N':
                    flag = False
                    print(message[i-j][0], 'was nasty about', message[i][0])
        if flag:
            print('Nobody was nasty')
        count += 1
        print()

