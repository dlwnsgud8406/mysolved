import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ascending_stack = 0
max_ascending_length = 0
for i in range(n-1):
    if arr[i] < arr[i+1]:
        ascending_stack += (arr[i+1] - arr[i])
        if ascending_stack > max_ascending_length:
            max_ascending_length = ascending_stack
    else:
        ascending_stack = 0
print(max_ascending_length)

