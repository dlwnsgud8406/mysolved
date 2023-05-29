n = int(input())
v_count = int(n/5)
i_count = int(n%5)

for i in range(v_count):
    print('V', end='')
for i in range(i_count):
    print('I', end='')
