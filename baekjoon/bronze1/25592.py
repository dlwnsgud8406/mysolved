n = int(input())
count = 1
Sum = 0
is_turn = False
while 1:
    if count % 2 == 1:
        is_turn = True
    else:
        is_turn = False
    Sum += count
    if Sum > n:
        break
    count += 1
if not is_turn:
    print(0)
else:
    print(Sum - n)

