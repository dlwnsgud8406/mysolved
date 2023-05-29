# 3
# 3 2 1
# 5 .16 4.54
# 3 3.7 3.6
n = int(input())
for i in range(n):
    a, b, c = map(float, input().split())
    print("$%.2f" %(a*b*c))
