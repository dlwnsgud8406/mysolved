n = int(input())
arr = []
for i in range(n):
    string = input()
    arr.append((string, len(string)))
arr = list(set(arr))
arr = sorted(arr, key=lambda x:(x[1], x[0]))
for j in range(len(arr)):
    print(arr[j][0])

