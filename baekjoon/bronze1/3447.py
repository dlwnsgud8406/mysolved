while 1:
    try:
        string = input()
    except EOFError:
        exit(0)
    while 1:
        if 'BUG' in string:
            if string == string.replace('BUG', ''):
                break
            else:
                string = string.replace('BUG', '')
        else:
            break
    print(string)

