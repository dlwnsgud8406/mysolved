n = int(input())
Sum = 0
count = 1
while 1:
    for i in range(count):
        Sum += i
        print(Sum)
    count += 1
    if Sum > n:
        break
