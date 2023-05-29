n = int(input())
all_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
all_num = 0
for i in range(len(all_string)):
    all_num += ord(all_string[i])
for i in range(n):
    string = list(set(list(input())))
    current_num = 0
    for j in range(len(string)):
        current_num += ord(string[j])

    print(all_num - current_num)

