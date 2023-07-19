import sys
input = sys.stdin.readline
board = [[0]*6 for _ in range(6)]
start = input()
cur = start
answer = 'Valid'
x, y = ord(cur[0]) - 65, int(cur[1]) - 1
board[x][y] = 1

for _ in range(35):
    now = input()
    a, b = ord(now[0]) - 65, int(now[1]) - 1
    if board[a][b] == 1:
        answer = 'Invalid'
        break
    elif str(abs(a-x)) + str(abs(b - y)) not in '12 21':
        answer = 'Invalid'
        break
    else:
        board[a][b] = 1
        cur = now
        x, y = a, b
a, b = ord(start[0]) - 65, int(start[1]) - 1
if abs(a- x) + abs(b - y) != 3:
    answer = 'Invalid'
print(answer)
