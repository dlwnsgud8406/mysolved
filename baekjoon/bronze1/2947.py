arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
while sorted_arr != arr:
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            temp = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = temp
            print(*arr, sep=' ')


