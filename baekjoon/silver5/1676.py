import math
num = math.factorial(int(input()))
arr = list(str(num))[::-1]
answer = 0
for number in arr:
    if number != '0':
        print(answer)
        exit(0)
    else:
        answer += 1
