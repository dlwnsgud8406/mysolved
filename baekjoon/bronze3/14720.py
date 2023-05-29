n = int(input())
arr = list(map(int, input().split()))
current_milk = 0
answer = 0
for milk in arr:
    if milk == current_milk:
        current_milk += 1
        answer += 1
    if current_milk > 2:
        current_milk = 0
print(answer)



