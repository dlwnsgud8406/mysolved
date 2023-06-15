while 1:
    string = input()
    if string == '0':
        exit(0)
    else:
        a, b = map(int, string.split())
        arr = []
        for i in range(a//4):
            arr = [(i * 4 + 1), (i * 4 + 2), (a - (4 * i)) - 1, (a - (4 * i))]
            if b in arr:
                arr.remove(b)
                arr = sorted(arr)
                for j in range(len(arr)):
                    print(arr[j], end=' ')
                print()
                break

