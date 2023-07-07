n = int(input())
arr = []
for i in range(n):
    arr.append(input())
for string in arr:
    if string[::-1] in arr:
        print(len(string), string[len(string)//2])
        exit(0)
