string = input()
arr = [0] * 26
for i in string:
    arr[ord(i) - 97] += 1
for j in arr:
    print(j, end=' ')


