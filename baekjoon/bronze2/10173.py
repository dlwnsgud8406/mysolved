while 1:
    string = input()
    if string == "EOI":
        exit(0)
    else:
        string = string.upper()
        if 'NEMO' in string:
            print('Found')
        else:
            print('Missing')


