import math

min, max = map(int, input().split())
answer = 0
current_number = min

for i in range(current_number, max):
    if math.sqrt(i) != int(math.sqrt(i)):
        answer = answer + 1

print(answer)