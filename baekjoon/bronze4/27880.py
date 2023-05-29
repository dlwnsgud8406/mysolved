answer = 0
for i in range(4):
    measure, time = input().split()
    if measure == "Es":
        answer += (int(time) * 21)
    elif measure == "Stair":
        answer += (int(time) * 17)
print(answer)


