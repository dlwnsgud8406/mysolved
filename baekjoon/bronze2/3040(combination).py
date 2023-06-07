from itertools import *
arr = []
answer = []
for i in range(9):
    arr.append(int(input()))
for i in list(combinations(arr, 7)):
    if sum(i) == 100:
        answer = i
for i in range(len(answer)):
    print(answer[i])

