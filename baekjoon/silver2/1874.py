n = int(input())
stack = []
answer = []
is_available = True
current_num = 1
for i in range(n):
    num = int(input())
    while current_num <= num:
        stack.append(current_num)
        answer.append('+')
        current_num += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        is_available = False
        break
if is_available:
    print(*answer, sep='\n')
