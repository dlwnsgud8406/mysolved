from collections import Counter
def solution(s):
    answer = ''
    string = set(s)
    arr = Counter(list(s))
    for char in string:
        if arr[char] == 1:
            answer += char
    return ''.join(sorted(answer))
