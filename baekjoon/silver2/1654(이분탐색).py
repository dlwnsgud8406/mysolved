import sys
input = sys.stdin.readline

n, required_line = map(int, input().split())
lan = [int(input()) for i in range(n)]

count = 1
end = max(lan)
while count <= end:
    mid = (count + end) // 2
    lines = 0
    for i in lan:
        lines += (i // mid)
    if lines >= required_line:
        count = mid + 1
    else:
        end = mid - 1
print(end)
