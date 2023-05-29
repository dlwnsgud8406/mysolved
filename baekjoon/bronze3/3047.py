arr = sorted(list(map(int, input().split())))
string = input()

for ch in string:
    if ch == 'A':
        print(arr[0], end=' ')
    elif ch == 'B':
        print(arr[1], end=' ')
    else:
        print(arr[2], end=' ')

