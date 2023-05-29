n, m  = map(int, input().split())

first_matrix = [list(map(int, input().split())) for _ in range(n)]
second_matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        first_matrix[i][j] += second_matrix[i][j]

for i in range(n):
    for j in range(m):
        print(first_matrix[i][j], end=' ')
    print()


