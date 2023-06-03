input()
arr = [0] * 5
string = input()
arr[0] += string.count('H')
arr[1] += string.count('I')
arr[2] += string.count('A')
arr[3] += string.count('R')
arr[4] += string.count('C')
print(min(arr))
