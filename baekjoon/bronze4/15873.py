string = input()
answer = 0
for i in range(len(string)):
    if int(string[i]) == 0:
        answer -= int(string[i-1])
        answer = answer + (int(string[i-1]) * 10)
    else:
        answer += int(string[i])
print(answer)
