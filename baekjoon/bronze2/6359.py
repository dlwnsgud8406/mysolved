T = int(input())
for i in range(T):
    n = int(input())
    arr = [1] * n
    for j in range(2, n+1):
        count = 1
        while j*count-1 < len(arr):
            if arr[j*count-1] == 0:
                arr[j*count-1] = 1
            elif arr[j*count-1] == 1:
                arr[j*count-1] = 0
            count += 1
    print(arr.count(1))

