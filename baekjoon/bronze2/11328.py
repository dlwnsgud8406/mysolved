T = int(input())
for i in range(T):
    string1, string2 = input().split()
    if sorted(string1) == sorted(string2):
        print('Possible')
    else:
        print('Impossible')
