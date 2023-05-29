n = int(input())
a = b = 100
for i in range(n):
    changyoung, sangdeok = map(int, input().split())
    if changyoung > sangdeok:
        b = b - changyoung
    elif changyoung < sangdeok:
        a = a - sangdeok

print(a)
print(b)
