string = input()
answer = 1
d_count = 10
c_count = 26
for char in string:
    if char == 'd':
        answer *= d_count
        d_count -= 1
        if d_count == 8:
            d_count += 1
        c_count = 26
    if char == 'c':
        answer *= c_count
        c_count -= 1
        if c_count == 24:
            c_count += 1
        d_count = 10
print(answer)

