n = int(input())
for i in range(n):
    count, price = map(int, input().split())
    if count == 1:
        print(count, price)
        print(count*price)
    else:
        print(count, price)
        print(count*price-(count-1)*2)
