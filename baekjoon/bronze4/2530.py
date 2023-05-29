hour, minute, second = map(int, input().split())
needed_second = int(input())
needed_minute = needed_second//60
needed_second -= needed_minute*60
needed_hour = needed_minute//60
needed_minute -= needed_hour*60
up_minute = 0
up_hour = 0
meta_hour = 0
second += needed_second
minute += needed_minute
hour += needed_hour
if second > 59:
    minute += 1
    second -= 60
if minute > 59:
    hour += 1
    minute -= 60
if hour > 23:
    hour %= 24
print(hour, minute, second)
