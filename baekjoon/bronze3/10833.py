school_count = int(input())
apple_rest_sum = 0
for i in range(school_count):
    a, b = map(int, input().split())
    apple_rest_sum += (b % a)
print(apple_rest_sum)
