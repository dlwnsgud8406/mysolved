n = int(input())
dalgu_score = 0
phonics_score = 0

for i in range(n):
    if abs(dalgu_score - phonics_score) >= 2:
        break
    string = input()
    if string == 'D':
        dalgu_score += 1
    elif string == 'P':
        phonics_score += 1
print("%d:%d"%(dalgu_score, phonics_score))

