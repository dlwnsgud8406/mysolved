# 260000
# 4
# 20000 5
# 30000 2
# 10000 6
# 5000 8
sum_ = int(input())
n = int(input())
user_sum = 0
for i in range(n):
    a, b = map(int, input().split())
    user_sum += a*b
if sum_ == user_sum:
    print('Yes')
else:
    print('No')
