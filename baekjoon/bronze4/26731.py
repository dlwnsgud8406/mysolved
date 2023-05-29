current_arr = []
for i in range(26):
    current_arr.append(chr(65+i))

string = input()
for char in string:
    if char in current_arr:
        current_arr.pop(current_arr.index(char))
print("%c" %current_arr[0])
