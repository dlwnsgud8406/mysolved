import sys

input = sys.stdin.readline
a, b, c, m = map(int, input().split())

if a > m:
    print(0)
else:
    current_fatigue = 0
    current_time = 0
    sum_work = 0
    while current_time != 24:
        if current_fatigue + a <= m:
            current_fatigue += a
            sum_work += b
        else:
            current_fatigue = max(0, current_fatigue-c)
        current_time += 1
    print(sum_work)

