n = int(input())
string = input()
vowel = 0

for i in string:
    if i in ['a', 'i', 'u', 'e', 'o']:
        vowel += 1
print(vowel)
