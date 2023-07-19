n = int(input())
count = n
for _ in range(n):
    string = input()
    check = []
    for char in string:
        if char in check and char != check[-1]:
            count -= 1
            break
        if char not in check:
            check.append(char)
print(count)
