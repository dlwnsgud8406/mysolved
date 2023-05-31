standard = [100, 100, 200, 200, 300, 300, 400, 400, 500]

score = list(map(int, input().split()))

answer = 0

if sum(score) < 100:
    print('none')
elif max(score) > standard[score.index(max(score))]:
    print('hacker')
elif sum(score) >= 100 and max(score) <= standard[score.index(max(score))]:
    print('draw')
