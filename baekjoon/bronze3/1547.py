n = int(input())
cup = [1, 2, 3]
for i in range(n):
    a, b = map(int, input().split()) # 입력받기
    a_cup = cup.index(a) # a번째 있는 컵의 번호 확인
    b_cup = cup.index(b) # b번째 있는 컵의 번호 확인
    cup[a_cup], cup[b_cup] = cup[b_cup], cup[a_cup] # 서로 한번에 바꾸기
print(cup[0])

