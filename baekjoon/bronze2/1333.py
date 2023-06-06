n, l, d = map(int, input().split())
call_time = []
for i in range(1, 99999):
    call_time.append(d*i)
current_time = 0
for i in range(1, n+1):
    no_music_time = i * l + (5 * (i - 1))
    rest_time = no_music_time + 5
    for j in range(len(call_time)):
        if no_music_time <= call_time[j] < rest_time:
            print(call_time[j])
            exit(0)
print((l+5) * n)
