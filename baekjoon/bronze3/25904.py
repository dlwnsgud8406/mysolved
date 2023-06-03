person, current_sound = map(int, input().split())
max_sound = list(map(int, input().split()))
while 1:
    for i in range(person):
        if max_sound[i] >= current_sound:
            current_sound += 1
        else:
            print(i+1)
            exit(0)
