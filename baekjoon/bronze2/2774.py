from collections import Counter
n = int(input())
for i in range(n):
    string = list(map(list, input().split()))
    string = sum(string, [])
    dict = Counter(string)
    print(len(dict))
