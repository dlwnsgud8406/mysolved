n = int(input())
for i in range(n):
    string = input()
    count = 0
    answer = 0
    for char in string:
        if char == 'O':
            count += 1
            answer += count
        elif char == 'X':
            count = 0
    print(answer)
