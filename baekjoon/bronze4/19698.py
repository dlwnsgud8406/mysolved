n, w, h, l = map(int, input().split())
row = w // l
col = h // l
print(min(row*col, n))
