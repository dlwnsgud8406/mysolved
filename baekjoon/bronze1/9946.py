count = 1
while 1:
    str1 = input()
    str2 = input()
    if str1 == str2 == 'END':
        exit(0)
    else:
        str1 = sorted(list(str1))
        str2 = sorted(list(str2))
        print('Case ' + str(count) + ': ', end='')
        if str1 == str2:
            print('same')
        else:
            print('different')
        count += 1
