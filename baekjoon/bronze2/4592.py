while True:
    num = input()
    answer = ''
    if num == '0':
        exit(0)
    else:
        num = num.split(' ')
        N = int(num[0])
        num = num[1:]
        answer += num[0] + ' '
        for i in range(1, N):
            if num[i - 1] != num[i]:
                answer += num[i] + ' '
        print(answer + '$')
