import sys
input = sys.stdin.readline

day = {'Mon' : 1, 'Tue' : 2, 'Wed' : 3, 'Thu' : 4, 'Fri' : 5, 'Sat' : 6, 'Sun' : 7}
time, n = map(int, input().split())
for i in range(n):
    a, b, c, d = input().split()
    b = int(b)
    d = int(d)
    a = day[a]
    c = day[c]
    time -= ((c-a)*24 + (d-b))
if time <= 0:
    print(0)
elif time > 48:
    print(-1)
else:
    print(time)
