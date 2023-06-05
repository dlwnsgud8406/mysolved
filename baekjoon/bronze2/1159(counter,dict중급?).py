from collections import Counter

answer = 0
answer_str = []
n = int(input())
name_arr = []
for i in range(n):
    string = input()
    name_arr.append(string[0])
counter = Counter(name_arr)
for i in counter.keys():
    if counter.get(i) >= 5:
        answer_str.append(i)
        answer += 1
if answer == 0:
    print('PREDAJA')
else:
    for i in sorted(answer_str):
        print(i, end='')


