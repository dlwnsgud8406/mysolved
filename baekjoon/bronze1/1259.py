while 1:
    string = input()
    if string == '0':
        exit(0)
    else:
        if string == string[::-1]:
            print('yes')
        else:
            print('no')
