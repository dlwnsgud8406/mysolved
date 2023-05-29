n = int(input())
for i in range(n):
    string = input()
    prev = ''
    for char in string:
        if prev != char:
            print(char, end ="")
            prev = char
    print()


