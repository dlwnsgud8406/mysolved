n = int(input())
answer = 1
cut = 1
for i in range(n):
    if i % 2 != 0:
        cut += 1
    answer += cut
print(answer)
