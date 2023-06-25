import sys
input = sys.stdin.readline

n = int(input())
arr = []
same = [0] * n
for i in range(n):
    arr.append(list(map(int, input().split())))
    same[i] = [0] * n

for i in range(5):
    for j in range(n):
        for k in range(j+1, n):
            if arr[j][i] == arr[k][i]:
                same[k][j] = 1
                same[j][k] = 1
count = []
for s in same:
    count.append(s.count(1))
print(count.index(max(count)) + 1)

