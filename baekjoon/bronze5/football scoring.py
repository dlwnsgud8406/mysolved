while 1:
    try:
        arr = list(map(int, input().split()))
    except EOFError:
        break
    else:
        print(arr[0]*6+ arr[1]*3+ arr[2]*2+ arr[3]*1+ arr[4]*2, end=' ')
