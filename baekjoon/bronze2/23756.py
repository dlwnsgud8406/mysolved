n = int(input())
current_angle = int(input())
answer = 0
for i in range(n):
    required_angle = int(input())
    answer += min(abs(required_angle - current_angle), 360 - abs(current_angle - required_angle))
    current_angle = required_angle
print(answer)
