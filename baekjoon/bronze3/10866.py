n = int(input())
is_cute = 0
is_not_cute = 0
for i in range(n):
    if input() == '1':
        is_cute += 1
    else:
        is_not_cute += 1
if is_cute > is_not_cute:
    print("Junhee is cute!")
elif is_cute < is_not_cute:
    print("Junhee is not cute!")

