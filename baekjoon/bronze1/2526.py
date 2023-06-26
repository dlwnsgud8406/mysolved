n, p = map(int, input().split())
arr =[]
current_num = n
count = 0
while 1:
    arr.append(current_num)
    count += 1
    current_num = current_num * n % p
    if current_num in arr:
        print(count - arr.index(current_num))
        exit(0)
