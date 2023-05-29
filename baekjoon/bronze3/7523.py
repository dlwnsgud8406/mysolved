import sys
input = sys.stdin.readline
n = int(input())
count = 1
for i in range(n):
    a, b = map(int, input().split())
    answer = int((a+b)*(b-a+1)//2)
    print('Scenario #%d:'%count)
    print(answer)
    print('')
    count += 1
