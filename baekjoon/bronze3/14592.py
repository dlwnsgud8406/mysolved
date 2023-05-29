n = int(input())

winner, max_s, min_c, min_l = 0, 0, 50, 179
for i in range(n):
    s, c, l = map(int, input().split())
    if s > max_s:
        winner, max_s, min_c, min_l = i + 1, s, c, l
    elif s == max_s and c < min_c:
        winner, max_s, min_c, min_l = i + 1, s, c, l
    elif s == max_s and c == min_c and l < min_l:
        winner, max_s, min_c, min_l = i + 1, s, c, l
print(winner)

