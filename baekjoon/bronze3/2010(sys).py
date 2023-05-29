import sys
n = int(input())
answer = 0
for i in range(n):
    if i == n-1:
        answer += (int(sys.stdin.readline()))
    else:
        answer += (int(sys.stdin.readline()) - 1)
print(answer)
