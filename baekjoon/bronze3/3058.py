n = int(input())
for i in range(n):
    even_arr = []
    all_arr = list(map(int, input().split()))
    for num in all_arr:
        if num % 2 == 0:
            even_arr.append(num)
    print(sum(even_arr), min(even_arr))
