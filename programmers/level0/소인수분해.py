def solution(n):
    answer = []
    cnt = 2
    while cnt <= n:
        if n % cnt == 0:
            answer.append(cnt)
            n = n // cnt
        else:
            cnt += 1
    return sorted((list(set(answer))))
