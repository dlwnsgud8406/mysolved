import sys
input = sys.stdin.readline

a, b = map(int, input().split())
answer = 1
for i in range(a, b + 1):
    in_sum = 0
    for j in range(i + 1):
        in_sum += j
    answer *= in_sum
print(answer % 14579)
