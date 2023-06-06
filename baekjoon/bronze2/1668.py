n = int(input())
trophy = []
for i in range(n):
    trophy.append(int(input()))
left_max = trophy[0]
left_answer = 1
right_max = trophy[len(trophy) - 1]
right_answer = 1
for i in range(n):
    if trophy[i] > left_max:
        left_max = trophy[i]
        left_answer += 1
    if trophy[len(trophy) - 1 - i] > right_max:
        right_max = trophy[len(trophy) - 1 - i]
        right_answer += 1
print(left_answer)
print(right_answer)
