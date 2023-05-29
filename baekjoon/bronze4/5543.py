hamburger = []
beverage = []
burger_set = []
hamburger.append(int(input()))
hamburger.append(int(input()))
hamburger.append(int(input()))
beverage.append(int(input()))
beverage.append(int(input()))

for i in range(len(hamburger)):
    for j in range(len(beverage)):
        burger_set.append(hamburger[i] + beverage[j] - 50)
burger_set.sort()

print(burger_set[0])
