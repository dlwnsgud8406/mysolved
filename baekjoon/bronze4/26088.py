n = int(input())
answer = 0
for i in range(n):
    day = input().split('-')[1]
    if int(day) <= 90:
        answer += 1
print(answer)
