n = input()
level = 0
while len(n) != 1:
    sum_happy = 1
    for num in n:
        sum_happy *= int(num)
    n = str(sum_happy)
    level += 1
print(level)

