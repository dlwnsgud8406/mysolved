T = int(input())
arr = list(map(int, input().split()))
for i in range(T):
    in_arr = []
    for j in range(1, arr[i] + 1):
        if arr[i] / j == int(arr[i] / j):
            in_arr.append(j)
    in_arr.pop()
    if sum(in_arr) == arr[i]:
        print('Perfect')
    elif sum(in_arr) > arr[i]:
        print('Abundant')
    else:
        print('Deficient')
