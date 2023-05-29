import math
import sys

while 1:
    n = sys.stdin.readline().rstrip('\n')
    sum = 0
    if n == '0':
        break
    for i in range(len(n)):
        sum += int(n[len(n)-i-1]) * math.factorial(int(i) + 1)
    print(sum)
