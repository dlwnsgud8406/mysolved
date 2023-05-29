from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

pos = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            pos.append(i)
            pos.append(j)

distance = 0

def bfs(x, y):
    visited = [[0]*N for _ in range(N)]
    queue = deque([[x, y]])
    cand = []

    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        for index in range(4):
            nx = i + dx[index]
            ny = j + dy[index]

            if 0 <= nx < N and 0 <=ny < N and visited[nx][ny] == 0:
                if board[x][y] > board[nx][ny] and board[nx][ny] != 0:
                    visited[nx][ny] = visited[i][j] + 1
                    cand.append((visited[nx][ny] -1, nx, ny))
                elif board[x][y] == board[nx][ny]:
                    visited[nx][ny] = visited[i][j] + 1
                    queue.append([nx, ny]
                elif board[nx][ny] == 0:
                    visited[nx][ny] = visited[i][j] + 1
                    queue.append([nx, ny])
    return sorted(cand, key = lambda x : (x[0],x[1],x[2]))

i, j = pos
size = [2, 0]

while True:
    board[i][j] = size[0]
    cand = deque(bfs(i,j))

    if not cand:
        break

    step, xx, yy = cand.popleft()
    distance = distance + step
    size[1] = size[1] + 1

    if size[0] == size[1]:
        size[0] = size[0] + 1
        size[1] = 0

    board[i][j] = 0
    i, j = xx, yy
print(distance)