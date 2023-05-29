n = int(input())
for i in range(n):
    yonsei_score = 0
    korea_score = 0
    for _ in range(9):
        a, b = map(int, input().split())
        yonsei_score += a
        korea_score += b
    if yonsei_score > korea_score:
        print('Yonsei')
    elif korea_score > yonsei_score:
        print('Korea')
    else:
        print('Draw')
