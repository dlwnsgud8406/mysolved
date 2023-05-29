from collections import deque

n, m = map(int, input().split()) # n, m 입력받기
board = [list(input().strip()) for _ in range(n)] # 숫자가 아닌 문자들을 입력받기
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)] 
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

queue = deque()

def init():
    rx, ry, bx, by = [0] * 4
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
    queue.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    count = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x = x + dx
        y = y + dy
        count = count + 1
    return x, y, count

def bfs():
    init()
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            break
        for i in range(len(dx)):
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i])
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i])

            if board[next_bx][next_by] == 'O':
                continue
            if board[next_rx][next_ry] == 'O':
                print(depth)
                return
            if next_rx == next_bx and next_ry == next_by : 
                if r_count > b_count:
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]

            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                queue.append((next_rx, next_ry, next_bx, next_by, depth+1))
    print(-1)

bfs()