n = int(input())
print('Gnomes:')
for i in range(n):
    compare_arr = []
    reverse_compare_arr = []
    arr = list(map(int, input().split()))
    if arr == sorted(arr) or arr == sorted(arr, reverse=True):
        print("Ordered")
    else:
        print("Unordered")
