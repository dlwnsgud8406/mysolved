# 전체 상금의 22%를 제세공과금으로 납부하는 경우
# 상금의 80%를 필요 경비로 인정받고, 나머지 금액 중 22%만을 제세공과금으로 납부하는 경우

price = int(input())
first = price * 0.78
second = price * 0.8 + (price*0.2)*0.78
print(int(first), int(second))
