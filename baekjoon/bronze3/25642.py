def check(num, name):
    if num >= 5:
        if name == 'yt':
            print('yj')
            exit(0)
        elif name == 'yj':
            print('yt')
            exit(0)

a, b = map(int, input().split())
while a < 5 or b < 5:
    b += a
    check(b, 'yj')
    a += b
    check(a, 'yt')
