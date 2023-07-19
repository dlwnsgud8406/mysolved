string = input()
before_string = ''
while 1:
    before_string = string
    if 'XXXX' in string:
        string = string.replace('XXXX', 'AAAA')
    elif 'XX' in string:
        string = string.replace('XX', 'BB')
    if before_string == string:
        break
if 'X' in string:
    print(-1)
else:
    print(string)
