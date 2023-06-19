#시간이 더 많이 걸림
# n = int(input())
# answer = 0
# for i in range(1, n+1):
#     if n/i == int(n/i):
#         answer += 1
# print(answer)

#시간이 더 적게 걸림
N = int(input())
count = 0
for i in range(1, int(N**.5)+1):
    if N%i == 0:
        count += 1 + (N != i**2)
print(count)
