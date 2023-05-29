import sys
input = sys.stdin.readline

n = int(input())
arr= []
for i in range(n):
    for j in range(n):
        for k in range(n):
            if j >= i + 2 and i*j*k != 0 and k%2 == 0 and i+j+k == n:
                arr.append((i,j,k))

print(len(arr))
