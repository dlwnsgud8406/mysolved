n = int(input())
for i in range(n):
    a, b, c, d, e = map(float, input().split())
    print("$%.2f"%(a * 350.34 + b * 230.90 + c * 190.55 + d * 125.30 + e * 180.90))
