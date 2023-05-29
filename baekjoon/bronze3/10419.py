n = int(input())

for i in range(n):
    class_time = int(input())
    if class_time == 1:
        print(0)
    else:
        max_class_time = 1
        while max_class_time + (max_class_time ** 2) <= class_time:
            max_class_time += 1
        print(max_class_time - 1)
