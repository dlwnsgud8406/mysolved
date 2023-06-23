import sys
input=sys.stdin.readline

n, m = map(int, input().split())
# 시청자수는 n-1
bad_watcher = 0
standard = list(map(int, input().split()))
for i in range(n-1):
    current_watch = list(map(int, input().split()))
    sum = 0
    for j in range(m):
        sum += abs(current_watch[j] - standard[j])
        if sum > 2000:
            bad_watcher += 1
if bad_watcher >= (n-1) / 2:
    print('YES')
else:
    print('NO')


