command = input()
ball = [1, 0, 0, 2]
for char in command:
    temp = 0
    if char == 'A':
        temp = ball[0]
        ball[0] = ball[1]
        ball[1] = temp
    elif char == 'B':
        temp = ball[0]
        ball[0] = ball[2]
        ball[2] = temp
    elif char == 'C':
        temp = ball[0]
        ball[0] = ball[3]
        ball[3] = temp
    elif char == 'D':
        temp = ball[1]
        ball[1] = ball[2]
        ball[2] = temp
    elif char == 'E':
        temp = ball[1]
        ball[1] = ball[3]
        ball[3] = temp
    elif char == 'F':
        temp = ball[2]
        ball[2] = ball[3]
        ball[3] = temp
print(ball.index(1) + 1)
print(ball.index(2) + 1)
