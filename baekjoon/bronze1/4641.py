import sys
input = sys.stdin.readline

while 1:
    arr = list(map(int, input().split()))
    if arr[0] == -1:
        exit(0)
    else:
        arr.pop()
        answer = 0
        for i in range(len(arr)):
            if arr[i] * 2 in arr:
                answer += 1
        print(answer)
