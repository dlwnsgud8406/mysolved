n = int(input())
for i in range(n):
    string = input()
    if 'Simon says' not in string:
        continue
    else:
        print(string.split('Simon says')[1])
