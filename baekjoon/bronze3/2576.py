odd_arr = []
for i in range(7):
    num = int(input())
    if num % 2 == 1:
        odd_arr.append(num)
if len(odd_arr) == 0:
    print(-1)
else:
    print(sum(odd_arr))
    print(min(odd_arr))
