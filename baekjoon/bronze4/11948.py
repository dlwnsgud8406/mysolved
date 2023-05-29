science_score = []
society_score = []
for _ in range(4):
    science_score.append(int(input()))
for _ in range(2):
    society_score.append(int(input()))
science_score.sort()
society_score.sort()
answer = science_score[1] + science_score[2] + science_score[3] + society_score[1]
print(answer)
