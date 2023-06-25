import sys
input=sys.stdin.readline
n = int(input())
string = list(input())

for i in range(n-1):
    compare_string = input()
    for j in range(len(string)):
        if string[j] == compare_string[j]:
            continue
        else:
            string[j] = '?'

print(*string, sep='')
