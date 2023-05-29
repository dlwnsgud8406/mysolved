while 1:
    string = input()
    count = 0
    if string == '#':
        break
    else:
        string = list(string)
        for char in string:
            if char in 'aeiouAEIOU':
                count += 1
        print(count)

