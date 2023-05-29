first_rate, additional_rate = map(int, input().split())  # 첫 1000 KWH 요금, 추가 사용량 요금
num_customers = int(input())  # 고객 수

for i in range(num_customers):
    consumption = int(input())  # 고객의 전기 사용량
    if consumption <= 1000:
        charge = consumption * first_rate
    else:
        charge = 1000 * first_rate + (consumption - 1000) * additional_rate

    print(consumption, charge)
