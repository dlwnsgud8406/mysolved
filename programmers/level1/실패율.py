def solution(N, stages):
    answer = []
    arr = []
    for i in range(1, N+1):
        num = stages.count(i)
        rm_set = {i}
        failure = 0
        try:
            failure = num / len(stages)
        except ZeroDivisionError:
            arr.append((i, 0))
            stages = [i for i in stages if i not in rm_set]
            arr = sorted(arr, key = lambda x:-x[1])
        else:
            arr.append((i, failure))
            stages = [i for i in stages if i not in rm_set]
            arr = sorted(arr, key = lambda x:-x[1])

    for i in range(N):
        answer.append(arr[i][0])
    return answer
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
