n, m, k, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(len(board))

def growtree():
    for i in range(n):
        for j in range(n):
            if board[i][j]>0:
                board[i][j] += 1

def borntree():
    

print(board)