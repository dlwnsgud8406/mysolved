n = int(input())
answer = 2
answer_help = 2
for _ in range(0, n):
    answer = (2 * answer_help - 1) ** 2
    answer_help = answer ** 0.5
print(int(answer))
