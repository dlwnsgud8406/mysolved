def solution(command):
    state = 0
    x = y = 0
    for char in command:
        if char == 'R':
            state += 90
        elif char == 'L':
            state -= 90
        elif char == 'G':
            if state%360 == 90:
                x += 1
            elif state%360 == 180:
                y -= 1
            elif state%360 == 270:
                x -= 1
            elif state%360 == 0:
                y += 1
        elif char == 'B':
            if state%360 == 90:
                x -= 1
            elif state%360 == 180:
                y += 1
            elif state%360 == 270:
                x += 1
            elif state%360 == 0:
                y -= 1
    return [x, y]
