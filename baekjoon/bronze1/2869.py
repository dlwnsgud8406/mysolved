import sys
import math
input = sys.stdin.readline
a, b, v = map(int, input().split())
day = 0
v -= a
length = a
print(math.ceil(v / (a-b)) + 1)
