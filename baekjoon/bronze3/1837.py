result, k = map(int, input().split())
state = True
for i in range(2, k):
    if result % i == 0:
        print('BAD', i)
        state = False
        break
if state:
    print('GOOD')
