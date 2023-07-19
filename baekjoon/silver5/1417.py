import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for i in range(n)]
count = 0
while max(arr) != arr[0]:
    arr[arr.index(max(arr))] -= 1
    arr[0] += 1
    count += 1
# if count == 0 and len(arr) > 1:
#     print(1)
if arr.count(max(arr)) > 1:
    print(count + 1)
else:
    print(count)
