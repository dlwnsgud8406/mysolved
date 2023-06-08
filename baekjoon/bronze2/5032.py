import sys
input = sys.stdin.readline
e, f, c = map(int, input().split())
e += f
answer = 0
while e//c:
    answer += e//c
    e = e // c + e % c
print(answer)
