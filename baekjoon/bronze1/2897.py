r, c = map(int, input().split())
parking_lot = []
answer = [0] * 5
for _ in range(r):
    parking_lot.append(input())

for i in range(r):
    for j in range(c):
        if i + 1 == r or j + 1 == c:
            break
        w = parking_lot[i][j]
        x = parking_lot[i][j+1]
        y = parking_lot[i+1][j]
        z = parking_lot[i+1][j+1]

        temp = w+x+y+z
        if '#' in temp:
            continue
        else:
            car = temp.count('X')
            if car == 0:
                answer[0] += 1
            elif car == 1:
                answer[1] += 1
            elif car == 2:
                answer[2] += 1
            elif car == 3:
                answer[3] += 1
            elif car == 4:
                answer[4] += 1
for i in range(len(answer)):
    print(answer[i])
