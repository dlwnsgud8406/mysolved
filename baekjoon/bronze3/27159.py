input()
answer = 0
prev = -1
for num in map(int, input().split()):
    if num - prev > 1:
        answer += num
    prev = num
print(answer)
