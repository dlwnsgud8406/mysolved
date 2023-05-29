n = int(input())
string = input()
answer = 0
for i in range(n):
    answer += int(string[i:i+1])
print(answer)
