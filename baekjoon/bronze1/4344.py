import sys
input = sys.stdin.readline
C = int(input())

for i in range(C):
    arr = list(map(int, input().split()))
    length = arr[0]
    arr.remove(arr[0])
    count = 0
    sum = 0
    for j in range(length):
        sum += arr[j]
    avg = sum / length
    for j in range(length):
        if arr[j] > avg:
            count += 1

    print("%.3f" %((count/length) * 100), end ='')
    print('%')
