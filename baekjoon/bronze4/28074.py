arr = ['M', 'O', 'B', 'I', 'S']
string = input()
for char in string:
    if char in arr:
        arr.pop(arr.index(char))
if len(arr) == 0:
    print('YES')
else:
    print('NO')
