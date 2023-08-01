def solution(numbers):
    max_length = len(str(max(numbers)))
    numbers = map(str, numbers)
    arr = sorted(numbers, key = lambda x:(x*4)[:4], reverse = True)
    answer = ''.join(arr)
    if answer[0] == '0':
        return '0'
    else: return answer
