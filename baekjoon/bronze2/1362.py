pet_count = 1
standard_weight = 0
real_weight = 0
while 1:
    a, b = input().split()
    if a == b == '0':
        break
    elif a == 'F':
        if real_weight <= 0:
            continue
        else:
            real_weight += int(b)
    elif a == 'E':
        if real_weight <= 0:
            continue
        else:
            real_weight -= int(b)
    elif a == '#' and b =='0':
        if standard_weight * 0.5 < real_weight < standard_weight * 2:
            print("%d :-)" %(pet_count))
        elif real_weight <= 0:
            print("%d RIP" %(pet_count))
        else:
            print("%d :-(" % (pet_count))
        pet_count += 1
    else:
        standard_weight = int(a)
        real_weight = int(b)
