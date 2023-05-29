arr = list(map(int, input().split()))
duplicate = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            duplicate += 1
if duplicate == 1:
    duplicate += 1

arr.sort()
if duplicate == 3:
    result = 10000 + arr[0]*1000
elif duplicate == 2:
    result = 1000 + arr[1]*100
else:
    result = arr[len(arr)-1] * 100
print(result)
