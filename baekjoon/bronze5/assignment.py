student = []
count = 0
while count != 28:
    number = int(input())
    student.append(number)
    count += 1

for i in range(1, 31):
    if i not in student:
        print(i)
