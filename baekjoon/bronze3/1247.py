for i in range(3):
    num = int(input())
    answer = 0
    for j in range(num):
        answer += int(input())
    if answer > 0:
        print('+')
    elif answer < 0:
        print('-')
    else:
        print('0')
