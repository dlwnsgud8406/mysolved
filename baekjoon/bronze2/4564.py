while 1:
    arr = []
    num = int(input())
    if num == 0:
        break
    else:
        num_str = str(num)
        arr.append(num)
        while len(num_str) > 1:
            current_num = 1
            for n in num_str:
                current_num *= int(n)
            arr.append(current_num)
            num_str = str(current_num)
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()

