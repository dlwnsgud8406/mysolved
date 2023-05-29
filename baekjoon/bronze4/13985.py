string = input()

a, cal, b, equal, c = string.split(' ')
if int(a)+int(b) == int(c):
    print('YES')
else:
    print('NO')

