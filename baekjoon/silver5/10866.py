import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    command = input()
    if 'push_back' in command:
        arr.append(int(command.split(' ')[1]))
    elif 'push_front' in command:
        arr.insert(0, int(command.split(' ')[1]))
    elif 'pop_front' in command:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop(0))
    elif 'pop_back' in command:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop(len(arr) - 1))
    elif 'front' in command:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif 'back' in command:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr) - 1])
    elif 'size' in command:
        print(len(arr))
    elif 'empty' in command:
        if len(arr) == 0:
            print(1)
        else:
            print(0)
