n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(int((a*a*0.5) // (b*b*0.5)))
