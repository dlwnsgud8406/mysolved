x_arr = []
y_arr = []
answer_x=0
answer_y=0
for _ in range(3):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)
for i in range(3):
    if x_arr.count(x_arr[i]) == 1:
        answer_x = x_arr[i]
    if y_arr.count(y_arr[i]) == 1:
        answer_y = y_arr[i]
print(answer_x, answer_y)
