n = int(input())
arr = list(map(int, input().split()))
answer = 0
before_score = 0
for num in arr:
    if num == 1:
        before_score += 1
        answer += before_score
    else:
        before_score = 0
print(answer)
