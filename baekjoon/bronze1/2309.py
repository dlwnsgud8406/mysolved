from itertools import combinations
arr = [int(input()) for _ in range(9)]
answer_arr =()
for i in combinations(arr, 7):
    if sum(i) == 100:
        answer_arr = sorted(i)
for i in range(7):
    print(answer_arr[i])

