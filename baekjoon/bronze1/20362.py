import sys
input = sys.stdin.readline
n, answer_name = input().split()
n = int(n)
answer = n
answer_index = 0
answer_string = ''
before_arr = []
for i in range(n):
    name, string = input().split()
    if name == answer_name:
        answer_index = i
        answer_string = string
        break
    else:
        before_arr.append(string)


print(before_arr.count(answer_string))
