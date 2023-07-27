def solution(arr):
    answer = []
    standard = 10
    for num in arr:
        if standard == num:
            pass
        else:
            standard = num
            answer.append(num)
    return answer
