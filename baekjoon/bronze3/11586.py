n = int(input())
string = []
for i in range(n):
    string.append(input())
shape = input()
if shape == '1':
    for line in string:
        print(line)
elif shape == '2':
    for line in string:
        print(line[::-1])
elif shape == '3':
    for i in range(n):
        print(string[n-1-i])
