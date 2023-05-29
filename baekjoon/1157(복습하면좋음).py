string = list(input().upper())
count_string = list(set(string))
count_arr = []

max_count = 0
for char in count_string:
    count_arr.append(string.count(char))
if count_arr.count(max(count_arr)) > 1:
    print('?')
else:
    print(count_string[(count_arr.index(max(count_arr)))])
