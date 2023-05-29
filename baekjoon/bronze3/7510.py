n = int(input())
count = 1
for i in range(n):
    a, b, c = sorted(map(int, input().split()))
    print('Scenario #%d:' % count)
    if a**2 + b**2 == c**2:
        print('yes')
    else:
        print('no')
    print('')
    count += 1
