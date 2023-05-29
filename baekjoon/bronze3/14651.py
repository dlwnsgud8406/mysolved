n = int(input())
arr = list(map(int, input().split()))
answer = 0
for i in range(1, n + 1):
    if i != arr.index(i) + 1:
        answer += 1
print(answer)
