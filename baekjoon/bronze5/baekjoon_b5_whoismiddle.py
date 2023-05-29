bear = []
count = 0
while count != 3:
    number = int(input())
    bear.append(number)
    count += 1
bear.sort()
print(bear[1])
