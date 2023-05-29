x, y, w, h = map(int, input().split())

w_min = abs(w-x)
h_min = abs(h-y)
zero_x_min = abs(0 - x)
zero_y_min = abs(0 - y)
answer = min(min(w_min, h_min), min(zero_x_min, zero_y_min))
print(answer)
