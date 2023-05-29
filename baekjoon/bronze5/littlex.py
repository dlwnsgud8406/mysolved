n, x = map(int, input().split())
arr = []
arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] < x:
        print(arr[i],end=' ')
