arr_len = int(input())
arr = list(map(int, input().split()))
odd_arr = []
even_arr = []

for i in range(arr_len):
    if arr[i] % 2 == 0:
        even_arr.append(arr[i])
    elif arr[i] % 2 == 1:
        odd_arr.append(arr[i])

if len(even_arr) > len(odd_arr) or len(odd_arr) - 1 > len(even_arr):
    print(0)
else:
    print(1)
# 홀수와 짝수의 갯수차이가 나면 안됨
