m, n = map(int, input().split())
dx = [0, 1, 0, -1] # 4방향
dy = [1, 0, -1, 0]

g = [[-1] * n for _ in range(m)] # map그리기

x = y = 0 # 좌표
g[x][y] = 0 # 처음 위치
count = 0 # 답
d = 0

while 1:
    changed = False
    go = False
    for i in range(d, d+4):
        nx, ny = x + dx[i%4], y + dy[i%4]
        if nx < 0 or ny < 0 or nx >= m or ny >=n or g[nx][ny] != -1:
            changed = True
            continue
        go = True
        g[nx][ny] = 0
        x, y, d = nx, ny, i%4
        break
    if changed == True and go == True:
        count += 1
    if go == False:
        break
print(count)
