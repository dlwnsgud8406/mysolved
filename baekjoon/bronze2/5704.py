from collections import Counter
while 1:
    string = input()
    if string == '*':
        break
    else:
        string = list(map(list, string.split()))
        string = sum(string, [])
        dict = Counter(string)
        if len(dict) == 26:
            print('Y')
        else:
            print('N')
