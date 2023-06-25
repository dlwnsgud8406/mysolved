number = list(input())
for i in range(len(number) - 1):
    left_num = 1
    right_num = 1
    for j in range(i+1):
        left_num *= int(number[j])
    for j in range(i+1, len(number)):
        right_num *= int(number[j])
    if left_num == right_num:
        print('YES')
        exit(0)
print('NO')

