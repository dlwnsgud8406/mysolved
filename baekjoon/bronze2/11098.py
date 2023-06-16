T = int(input())
for i in range(T):
    n = int(input())
    arr = []
    for j in range(n):
        price, name = input().split()
        price = int(price)
        arr.append((name, price))
    arr.sort(key=lambda x:(-x[1]))
    print(arr[0][0])
