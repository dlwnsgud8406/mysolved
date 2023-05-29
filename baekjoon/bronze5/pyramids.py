answer = 0
while 1:
    N = int(input())
    if N == 0 :
        break
    else :
        for i in range(1, N+1):
            answer += i
        print(answer)
        answer = 0
