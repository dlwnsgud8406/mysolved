count = 1
while 1:
    string = input()
    if 'E' in string:
        break
    else:
        print("Case %d: "%count, end='')
        result = eval(string)
        if result == 0:
            print('false')
        else:
            print('true')
        count += 1

