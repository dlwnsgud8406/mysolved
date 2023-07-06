n = int(input())
string = input()
string += '#'
current_num = ''
answer = 0
for i in range(len(string)):
    if '0' <= string[i] <= '9':
        current_num += string[i]
    else:
        if (len(current_num) >= 1) or ('0' <= string[i-1]<='9' and string[i] == '#'):
            answer += int(current_num)
        current_num = ''

print(answer)
