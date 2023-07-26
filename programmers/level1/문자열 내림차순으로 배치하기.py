def solution(s):
    arr = sorted(s, reverse=True)
    answer = ''
    for char in arr:
        answer += char
    return answer
