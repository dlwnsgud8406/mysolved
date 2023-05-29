n = int(input())
answer = 0
count = 0
for i in range(1, n):
    if '50' in str(i):
        count += 1
if n <= 50:
    print(n)
else:
    print(n + count)
