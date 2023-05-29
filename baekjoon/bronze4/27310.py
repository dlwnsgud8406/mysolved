colon_count = 0
under_bar_count = 0
string = input()
for char in string:
    if char == ":":
        colon_count += 1
    if char == "_":
        under_bar_count += 1
print(colon_count + under_bar_count*5 + len(string))
