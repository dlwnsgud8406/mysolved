def solution(common):
    answer = 0
    if abs(common[1] - common[2]) == abs(common[1]-common[0]):
        d = common[1]-common[0]
        return (common[-1] + d)
    else:
        r = common[1] / common[0]
        return common[-1] * r
