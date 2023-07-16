mask = list(map(int, input().split()))
t_shirt = list(map(int, input().split()))
pants = list(map(int, input().split()))
a = min(mask[0], t_shirt[1], pants[0])
b = min(mask[1], t_shirt[0], pants[1])
if a == b:
    print(a+b)
else:
    print(2 * min(a,b) + 1)
