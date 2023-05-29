time = int(input())
if time % 10 != 0:
    print(-1)
else:
    print(time // 300, (time % 300) // 60, (time % 60) // 10)
