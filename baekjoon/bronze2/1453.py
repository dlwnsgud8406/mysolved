from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
dict = Counter(arr)
print(n - len(dict))
