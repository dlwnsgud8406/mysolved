n = int(input())
price = int(input())
arr = []

if n >= 20 :
    arr.append(price * 0.75)
if n >= 15:
    arr.append(price - 2000)
if n >= 10:
    arr.append(price * 0.9)
if n >= 5:
    arr.append(price - 500)
if n < 5:
    arr.append(price)

if min(arr) < 0:
    print(0)
else:
    print(int(min(arr)))


