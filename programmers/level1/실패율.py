def solution(N, stages):
    string = ''
    answer = []
    arr = []
    for char in stages:
        string += str(char)
    for i in range(1, N+1):
        num = string.count(str(i))
        try:
            failure = num / len(string)
        except ZeroDivisionError:
            continue
        else:
            arr.append((i, failure))
        string = string.replace(str(i), '')
    arr = sorted(arr, key = lambda x: (-x[1], x[0]))
    for i in range(N):
        answer.append(arr[i][0])
    return answer
print(solution(4, [4, 4, 4, 4, 4]))
