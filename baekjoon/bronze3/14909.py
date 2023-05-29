arr = list(map(int, input().split()))
answer = 0
for num in arr:
    if num > 0:
        answer += 1
print(answer)
