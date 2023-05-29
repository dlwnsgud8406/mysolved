count = 1
while 1:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    else:
        arr.pop(0)
    arr.sort()
    if len(arr) %2 == 0:
        print("Case %d: %.1f"%(count, (arr[len(arr)//2-1] + arr[len(arr)//2])/2))
    else:
        print("Case %d: %.1f"%(count, arr[len(arr)//2]))
