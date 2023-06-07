from collections import Counter

arr = []
for i in range(10):
    arr.append(int(input()))
print(int(sum(arr) / len(arr)))
dict = Counter(arr)
print(max(dict, key=dict.get))

