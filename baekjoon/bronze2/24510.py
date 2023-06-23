T = int(input())
max = 0
for i in range(T):
    string = input()
    current_max = string.count('for') + string.count('while')
    if max<current_max:
        max = current_max
print(max)
