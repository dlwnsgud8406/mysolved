semester_count = int(input())

for i in range(semester_count):
    class_count = int(input())
    class_complete_score = 0
    total_score = 0
    for j in range(class_count):
        a, b = map(float, input().split())
        total_score += (a * b)
        class_complete_score += a
    print("%d %.1f"%(class_complete_score, total_score/class_complete_score))

