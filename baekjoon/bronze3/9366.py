n = int(input())
count = 1
for i in range(n):
    arr = list(set(list(map(int, input().split()))))
    if len(arr) == 1:
        print('Case #%d: equilateral'%(count))
    elif len(arr) == 2:
        print('Case #%d: isosceles' % (count))
    elif len(arr) == 3:
        if arr[0] + arr[1] <= arr[2]:
            print('Case #%d: invalid!' % (count))
        else:
            print('Case #%d: scalene' % (count))
    count += 1
