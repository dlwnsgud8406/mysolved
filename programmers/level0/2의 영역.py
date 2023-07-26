def solution(arr):
    answer = []
    try:
        rest_list = list(filter(lambda x: arr[x] == 2, range(len(arr))))
        Max = max(rest_list)
        Min = min(rest_list)
    except ValueError:
        return [-1]
    else:
        for i in range(Min, Max+1):
            answer.append(arr[i])

    return answer

print(solution([1, 2, 1, 2, 1, 10, 2, 1]))
