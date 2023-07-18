import sys
input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n):
    command = input()
    if 'push' in command:
        stack.append(int(command.split(' ')[1]))
    elif 'top' in command:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'pop' in command:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(len(stack) - 1))
