def solution(n, m, section):
    arr = [1 for i in range(n)]
    answer = 0
    for num in section:
        arr[num - 1] = 0
    while min(arr) == 0:
        index = arr.index(0)
        arr[index:index + m] = [1 for i in range(index, index+m)]
        answer += 1
    return answer

print(solution(8, 4, [2,3,6]))
