arr = list(input())
res = []

for i in range(1, len(arr) - 1):
    for j in range(i+1, len(arr)):
        first = arr[:i]
        second = arr[i:j]
        third = arr[j:]

        first.reverse()
        second.reverse()
        third.reverse()
        res.append("".join(first+second+third))
print(min(res))
