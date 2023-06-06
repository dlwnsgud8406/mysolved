import sys
from collections import Counter
input = sys.stdin.readline
string_line = 0
string_list = []
answer_arr = []
for i in range(50):
    string = list(map(list, input().split()))
    # if len(string) == 0:
    #     break
    # else:
    string_list.extend(string)
string_list = sum(string_list, [])
dict = Counter(string_list)
tmp = [k for k, v in dict.items() if max(dict.values()) == v]
print(''.join(sorted(tmp)))
