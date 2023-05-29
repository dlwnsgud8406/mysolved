arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
reverse_sorted_arr = sorted(arr, reverse=True)
if sorted_arr == arr:
    print('ascending')
elif reverse_sorted_arr == arr:
    print('descending')
else:
    print('mixed')
