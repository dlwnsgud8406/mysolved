N, m, M, T, R = map(int, input().split())
time = 0
current_pulse = m
if m + T > M:
    print(-1)
else:
    while N:
        time += 1
        if current_pulse + T > M:
            current_pulse = max(current_pulse - R, m)
        else:
            current_pulse += T
            N -= 1
    print(time)
