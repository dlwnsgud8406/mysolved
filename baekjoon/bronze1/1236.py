n, m = map(int, input().split())
answer = 0
castle = []
for _ in range(n):
    castle.append(input())
line = across = 0
for i in range(n):
    if 'X' not in castle[i]:
        line += 1

for i in range(m):
    if 'X' not in [castle[j][i] for j in range(n)]:
        across += 1

print(max(line, across))
