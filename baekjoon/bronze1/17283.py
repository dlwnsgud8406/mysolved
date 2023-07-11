branch = int(input())
rate = int(input())
answer = 0
count = 1
while 1:
    branch = branch * (rate/100)
    branch = int(branch)
    if branch <=5:
        break
    else:
        answer += branch * (2 ** count)
        count += 1
print(answer)
