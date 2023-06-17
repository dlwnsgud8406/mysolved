dict_num = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' :8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13
        , 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24,
        'Y' : 25, 'Z' : 26}

T = int(input())
for i in range(T):
    num, is_num = input().split()
    num = int(num)
    arr = list(input().split())
    if is_num == 'C':
        for j in range(num):
            print(dict_num[arr[j]], end=' ')
    elif is_num == 'N':
        for j in range(num):
            for key, value in dict_num.items():
                if value == int(arr[j]):
                    print(key, end = ' ')
    print()
