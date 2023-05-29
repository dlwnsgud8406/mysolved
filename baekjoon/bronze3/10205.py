n = int(input())
count = 1
for i in range(n):
    current_head = int(input())
    action = input()
    for char in action:
        if char == 'c':
            current_head += 1
        elif char == 'b':
            current_head -= 1
    print('Data Set %d:'%count)
    print(current_head)
    print('')
    count += 1
