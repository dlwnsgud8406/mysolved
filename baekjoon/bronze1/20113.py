import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
vote = [0] * n
for i in range(n):
    if arr[i] == 0:
        pass
    else:
        vote[(arr[i]-1)] += 1
if vote.count(max(vote)) > 1:
    print('skipped')
else:
    print(vote.index(max(vote)) + 1)
