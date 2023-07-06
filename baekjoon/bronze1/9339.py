T = int(input())
for i in range(T):
    student = int(input())
    arr_student = list(map(int, input().split()))
    record_student = []
    runner = int(input())
    for j in range(runner):
        number, hour, minute = map(int, input().split())
        if (number in arr_student) and (hour != -1) and ((hour <= 5) or (hour == 6 and minute == 0)):
            record_student.append((number, hour, minute))
        record_student.sort(key=lambda x:(x[1], x[2]))
    print(record_student[0][0],len(record_student))

