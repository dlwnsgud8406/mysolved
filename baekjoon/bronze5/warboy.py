# 10 100 7
opposite_price, opposite_capacity, our_price = map(int, input().split())
print(int(((opposite_capacity/opposite_price) * 3) *our_price))
