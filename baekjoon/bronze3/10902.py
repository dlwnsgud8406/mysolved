n = int(input())
max_score = 0
min_time = 301
index = 0
for i in range(n):
    t, s = map(int, input().split())
    if s > max_score:
        max_score = s
        min_time = t
        index = i
    elif s == max_score != 0:
        if min_time > t:
            min_time = t
            index = i
if max_score == 0:
    print(0)
else:
    print(min_time + (index * 20))
