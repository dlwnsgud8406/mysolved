import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
    arr = []
    num = int(input())
    if num == 1:
        print(num)
        continue
    else:
        while num != 1:
            arr.append(num)
            if num % 2 == 1:
                num = num*3 + 1
            else:
                num = int(num / 2)
    print(max(arr))
