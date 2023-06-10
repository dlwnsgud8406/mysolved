string = input()
print(string[0], end='')
for i in range(1, len(string)):
    if string[i-1] != string[i]:
        print(string[i], end='')
