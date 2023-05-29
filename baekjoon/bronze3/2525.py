hour, minute = map(int, input().split())
required_minute = int(input())
minute += required_minute
if minute >= 60:
    hour = hour + minute//60
    minute = minute % 60

if hour >= 24:
    hour -= 24
print(hour, minute)
