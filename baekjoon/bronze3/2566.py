arr = [0] * 9
col_count = 0
for i in range(9):
    input_arr = list(map(int, input().split()))
    if max(arr) <= max(input_arr):
        arr = input_arr
        col_count = i + 1

print(max(arr))
print(col_count, arr.index(max(arr))+1)
