input()
string = input()
a = 0
b = 0
for char in string:
    if char == 'A':
        a += 1
    elif char == 'B':
        b += 1
if a>b:
    print('A')
elif a<b:
    print('B')
else:
    print('Tie')
