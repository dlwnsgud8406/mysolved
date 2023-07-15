import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
is_studying = False
study_time = 0
answer = 0
for i in range(n):
    if not is_studying:
        study_time = 30
    if study_time - arr[i] >= 0:
        if study_time >= arr[i] / 2:
            answer += 1
        study_time -= arr[i]
        if study_time <= 0:
            is_studying = False
        else:
            is_studying = True
    elif study_time < arr[i]:
        if study_time >= arr[i] / 2:
            answer += 1
        is_studying = False


print(answer)
