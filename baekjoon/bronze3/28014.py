n = int(input())
statue = list(map(int, input().split()))
answer = 0
prev = -1
for i in range(n):
    if prev <= statue[i]:
        answer += 1
    prev = statue[i]

print(answer)
