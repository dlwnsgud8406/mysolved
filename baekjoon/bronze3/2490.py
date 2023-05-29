for i in range(3):
    arr = sorted(list(map(int, input().split())))
    zero_count = 0
    one_count = 0
    for num in arr:
        if num == 0:
            zero_count += 1
        else:
            one_count += 1
    if zero_count == 0:
        print('E')
    elif zero_count == 1:
        print('A')
    elif zero_count == 2:
        print('B')
    elif zero_count == 3:
        print('C')
    else:
        print('D')

