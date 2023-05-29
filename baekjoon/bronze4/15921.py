n = int(input())
if n == 0:
    print("divide by zero")
    exit(0)
arr = list(map(int, input().split()))
sum_average = sum(arr) / len(arr)
each_average = 0
for i in range(len(arr)):
    each_average += arr[i] / len(arr)
print("%.2f"%(sum_average/each_average))
