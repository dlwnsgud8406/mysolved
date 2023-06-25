arr = list(map(int, input().split()))
min_num = min(arr)

while True:
    count = 0
    for i in range(len(arr)):
        if min_num % arr[i] == 0 :
            count += 1
    if count >= 3:
        print(min_num)
        break
    min_num += 1
