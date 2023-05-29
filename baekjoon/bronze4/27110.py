n = int(input())
a, b, c = map(int, input().split())
answer = 0
if a >= n:
    answer += n
else:
    answer += a
if b >= n:
    answer += n
else:
    answer += b
if c >= n:
    answer += n
else:
    answer += c

print(answer)
