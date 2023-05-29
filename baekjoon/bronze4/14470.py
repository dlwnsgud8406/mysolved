current_temperature = int(input())
goal_temperature = int(input())
frozen_per_temperature = int(input())
frozen_to_hot = int(input())
hot_per_temperature = int(input())
time = 0
if current_temperature < 0:
    time += (frozen_per_temperature * abs(current_temperature))
    current_temperature = 0
    time = time + frozen_to_hot
time += (goal_temperature - current_temperature)*hot_per_temperature
print(time)
