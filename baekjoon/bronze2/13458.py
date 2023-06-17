import math
n = int(input()) # 시험장의 개수
people = list(map(int, input().split()))
master_available, vice_available = map(int, input().split())
answer = 0
for i in range(n):
    people[i] -= master_available
    if people[i] < 0:
        people[i] = 0
    answer += 1
for i in range(n):
    answer += math.ceil(people[i] / vice_available)
print(answer)

