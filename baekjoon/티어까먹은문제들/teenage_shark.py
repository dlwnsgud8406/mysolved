import copy

board = [[] for _ in range(4)]

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [0, -1, 1, 0, -1, 1, -1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        fish.append([data[2*j], data[2*j+1]-1])
    board[i] = fish

max_score = 0

def dfs(sx, sy, score, board):
    global max_score
    score = score + board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = board[f_x][f_y][1]

        for i in range(8):
            nd = (f_d + i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            if not(0<=nx<4 and 0<= ny < 4) or 
