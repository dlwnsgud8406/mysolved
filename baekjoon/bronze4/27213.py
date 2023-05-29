row = int(input())
col = int(input())
if row == 1 or col == 1:
    answer = max(row, col)
else :
    answer = row + row + col - 2 + col - 2
print(answer)
