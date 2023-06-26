while 1:
    n = int(input())
    if n == 0:
        exit(0)
    else:
        arr = []
        for i in range(n):
            arr.append(input())
        arr.sort(key=str.lower)
        print(arr[0])
