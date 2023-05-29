a_count = 0
b_count = 0
string = input()
for char in string:
    if char == 'A':
        a_count += 1
    elif char == 'B':
        b_count += 1
print("%d : %d"%(a_count, b_count))
