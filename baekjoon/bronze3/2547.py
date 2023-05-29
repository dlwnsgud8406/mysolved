import sys
n = int(input())

for i in range(n):
    empty_string = input()
    students = int(sys.stdin.readline())
    candy = 0
    for j in range(students):
        candy += (int(sys.stdin.readline()))
    if candy % students == 0:
        print('YES')
    else:
        print('NO')
