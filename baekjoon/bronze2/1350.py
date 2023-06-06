import math

n = int(input())
arr = list(map(int, input().split()))
cluster_size = int(input())
answer = 0
for i in range(n):
    answer += (math.ceil(arr[i] / cluster_size) * cluster_size)
print(answer)
