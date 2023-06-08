daytime = int(input())
evening = int(input())
weekend = int(input())
a_daytime = daytime - 100 if daytime - 100 > 0 else 0
b_daytime = daytime - 250 if daytime - 250 > 0 else 0

a_costs = (a_daytime * 25 + 15 * evening + 20 * weekend) / 100
b_costs = (b_daytime * 45 + 35 * evening + 25 * weekend) / 100
print("Plan A costs %.2f" %a_costs)
print("Plan B costs %.2f" %b_costs)
if a_costs < b_costs:
    print('Plan A is cheapest.')
elif a_costs > b_costs:
    print('Plan B is cheapest.')
else:
    print('Plan A and B are the same price.')
