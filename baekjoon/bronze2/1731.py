import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
if arr[2] - arr[1] == arr[1] - arr[0]:
    print(arr[len(arr) - 1] + (arr[len(arr) - 1] - arr[len(arr) - 2]))
elif arr[2] / arr[1] == arr[1] / arr[0]:
    print(int(arr[len(arr) - 1] * (arr[len(arr) - 1]) / arr[len(arr) - 2]))
