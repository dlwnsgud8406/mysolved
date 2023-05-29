import math

l = int(input())
korean_todo = int(input())
math_todo = int(input())
korean_available = int(input())
math_available = int(input())

korean_day = math.ceil(korean_todo/korean_available)
math_day = math.ceil(math_todo/math_available)

if korean_day > math_day:
    print(l - korean_day)
else:
    print(l - math_day)
