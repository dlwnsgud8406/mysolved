num = int(input())
for i in range(num):
    ships, speed, days = map(int, input().split())

    ducats = 0
    for j in range(ships):
        distance, num_ducats = map(int, input().split())

        if(days * speed >= distance):
            ducats = ducats + num_ducats
    format_ = f"Data Set {i+1}:"
    print(format_); print(ducats); print()
