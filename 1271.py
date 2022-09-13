
money, count = input().split() #이런식으로 문자열을 여러개 입력받고 쪼갤 수 있음
money = int(money)
count = int(count)

print(int(money//count))
# /는 결과가 float //는 결과가 int
print(money%count)