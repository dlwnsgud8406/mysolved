n, l = map(int, input().split())
answer = []
label = 1
while len(answer) != n:
    if str(l) in str(label):
        pass
    else:
        answer.append(label)
    label += 1
print(max(answer))
