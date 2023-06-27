score = [0]
for _ in range(10):
    score.append(score[-1] + int(input())) # sum들을 볼 수 있음
print(min(score, key = lambda x:(abs(100-x), 100-x)))
