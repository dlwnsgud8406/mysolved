answer = 0
a, b = sorted(map(int, input().split()))
a_x, a_y = a // 4, a % 4
b_x, b_y = b // 4, b % 4

if a_y == 0:
    a_x -= 1
    a_y = 4
if b_y == 0:
    b_x -= 1
    b_y = 4
answer = abs(a_x - b_x) + abs(a_y - b_y)
print(answer)
