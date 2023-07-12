string = input()
answer = len(string)
for i in range(len(string)-1):
    if string[i] < string[i+1]:
        i += 1
        answer -= 1
    else:
        pass
print(answer)
