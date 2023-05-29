while True:
    n = input()
    if n == '0':
        break
    else:
        while len(n) > 1:
            temp = 0
            for num in n:
                temp += int(num)
            n = str(temp)
        print(n)
