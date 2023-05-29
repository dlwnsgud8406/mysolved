n = int(input())
for i in range(n):
    num = int(input())
    bin_num = bin(num).split('b')[1]
    for j in range(len(bin_num)):
        if bin_num[len(bin_num) - j - 1] == '1':
            print(j, end = ' ')

