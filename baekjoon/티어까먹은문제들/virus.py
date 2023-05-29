import math

store = int(input())

customer = []
customer = input().split()
customer = list(map(int, customer))

boss, employee = input().split()
boss = int(boss)
employee = int(employee)

answer = 0

for i in range(0, len(customer)):
    if customer[i] < boss:
        customer[i] = 0
        answer = answer + 1
    else:
        customer[i] = customer[i] - boss
        answer = answer + 1

for i in range(0, len(customer)):
    if 0<customer[i]<employee:
        answer = answer + 1
    elif customer[i]==0:
        pass
    else:
        customer[i] = math.ceil(customer[i] / employee)
        answer = answer + customer[i]

print(answer)