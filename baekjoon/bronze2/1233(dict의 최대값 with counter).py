from collections import Counter
a, b, c = map(int, input().split())
arr = []
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            arr.append(i + j + k)
dict = Counter(arr)
print(max(dict, key=dict.get))
