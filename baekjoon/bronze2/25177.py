import sys
input = sys.stdin.readline
a, b = map(int, input().split())
current_arr = list(map(int, input().split()))
before_arr = list(map(int, input().split()))
answer_arr = []
if len(current_arr) < len(before_arr):
    for i in range(len(current_arr), len(before_arr)):
        current_arr.append(0)
elif len(current_arr) > len(before_arr):
    for i in range(len(before_arr), len(current_arr)):
        before_arr.append(0)

for i in range(len(current_arr)):
    if before_arr[i] - current_arr[i] < 0:
        answer_arr.append(0)
    else:
        answer_arr.append(before_arr[i] - current_arr[i])
print(max(answer_arr))

