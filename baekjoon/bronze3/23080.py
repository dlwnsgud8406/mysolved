n = int(input())
string = input()
count = 0
while count*n < len(string):
    print(string[(count) * n], end='')
    count += 1
