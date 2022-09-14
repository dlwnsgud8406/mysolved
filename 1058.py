T = int(input())

friends = [[0] for _ in range(T)] 

for i in range(0, T):
    friends[i] = input()

max = 0
for i in range(0, T):
    count = 0
    for j in range(0, len(friends[i])):
        if friends[i][j]=='Y':
            count+=1
    if max<count:
        max = count
print(max)