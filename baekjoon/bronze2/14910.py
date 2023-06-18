arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
if arr == sorted_arr:
    print('Good')
else:
    print('Bad')

