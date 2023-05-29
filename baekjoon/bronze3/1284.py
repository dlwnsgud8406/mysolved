while 1:
    answer = 0
    num = input()
    if num == '0':
        break
    else:
        answer = len(num)-1 + 2
        for one_num in num:
            if one_num == '0':
                answer += 4
            elif one_num == '1':
                answer += 2
            else:
                answer += 3
        print(answer)

