
def solution(keymap, targets):
    answer = []
    dict = {}
    state = False
    for i in range(65, 91):
        Min = 101
        for string in keymap:
            try:
                idx = string.index(chr(i))
            except ValueError:
                pass
            else:
                if Min > idx:
                    Min = idx
        if Min < 101:
            dict[chr(i)] = Min + 1
    for string in targets:
        Sum = 0
        state = True
        for char in string:
            try:
                num = dict[char]
            except KeyError:
                state = False
                break
            else:
                Sum += num
        if state:
            answer.append(Sum)
        else:
            answer.append(-1)
    return answer
print(solution(["ABCDE","ABBCE"], ["ABBEF"]))
# -1
# print(solution(['AA'], ['BA']))
# print(solution(["BC"], ["AC", "BC"]))
# 기댓값 〉 [-1, 3]
