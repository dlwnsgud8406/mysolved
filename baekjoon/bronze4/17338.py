arr = list(map(int, input().split()))
arr_index = arr.index(min(arr))
if sum(arr) >= 100 :
    print('OK')
else:
    if arr_index == 0:
        print('Soongsil')
    elif arr_index == 1:
        print('Korea')
    elif arr_index == 2:
        print('Hanyang')
