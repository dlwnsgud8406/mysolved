n = int(input())
board = [[0]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

students = [list(map(int, input().split())) for _ in range(n**2)]

print(board)