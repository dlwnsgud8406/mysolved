a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_score = 0
b_score = 0
last_a = 0
last_b = 0
for i in range(len(a)):
    if a[i] > b[i]:
        a_score += 3
        last_a = a[i]
        last_b = b[i]
    elif a[i] < b[i]:
        b_score += 3
        last_a = a[i]
        last_b = b[i]
    else:
        a_score += 1
        b_score += 1
print(a_score, b_score)

if a == b:
    print('D')
elif a_score > b_score:
    print('A')
elif b_score > a_score:
    print('B')
elif a_score == b_score:
    if last_a > last_b:
        print('A')
    if last_b > last_a:
        print('B')

