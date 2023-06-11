a, b = input().split()
len_minus = 0
length_a = len(a)
length_b = len(b)
if length_a > length_b:
    len_minus = length_a - length_b
    print(a[0:len_minus],end='')
    for i in range(len_minus, length_a):
        print(int(a[i]) + int(b[i-len_minus]), end='')
elif length_b > length_a:
    len_minus = length_b - length_a
    print(b[0:len_minus],end='')
    for i in range(len_minus, length_b):
        print(int(b[i]) + int(a[i-len_minus]), end='')
else:
    for i in range(len_minus, length_a):
        print(int(b[i]) + int(a[i]), end='')
