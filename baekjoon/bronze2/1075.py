n = int(input())
f = int(input())
arr = []
for i in range(10):
    for j in range(10):
        current_num_str = str(n)[:-2] + str(i) + str(j)
        but = int(current_num_str) % f
        arr.append((current_num_str[-2:], but))
arr.sort(key=lambda x: (x[1]))
print(arr[0][0])
