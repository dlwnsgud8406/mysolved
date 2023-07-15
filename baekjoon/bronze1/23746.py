import sys
input = sys.stdin.readline
n = int(input())
string = []
compress_string = []
for i in range(n):
    a, b = input().split()
    string.append(a)
    compress_string.append(b)
answer = input()
for i in range(n):
    answer = answer.replace(compress_string[i], string[i])
a, b = map(int, input().split())
print(answer[a-1:b])
