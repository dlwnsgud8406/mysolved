import sys
input=sys.stdin.readline

n, k, l = map(int, input().split())
answer_arr = []
for i in range(n):
    a, b, c = map(int, input().split())
    if a+b+c >= k and ((a>=l) and(b>=l) and(c>=l)):
        answer_arr.append(a)
        answer_arr.append(b)
        answer_arr.append(c)
print(len(answer_arr)//3)
for i in range(len(answer_arr)):
    print(answer_arr[i],end=' ')
