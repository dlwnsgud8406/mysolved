import sys
input = sys.stdin.readline
count = 1
while 1:
    n = int(input())
    if n == 0:
        exit(0)
    else:
        arr = []
        index = []
        for i in range(n):
            arr.append(input())
            index.append(0)
        for i in range(2*n - 1):
            string = input()
            num = int(string.split(' ')[0])
            index[num-1] += 1
    for i in range(n):
        if index[i] != 2:
            print(count, arr[i])
    count += 1
