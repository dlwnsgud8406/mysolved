current_person = 0
max_person = 0
for i in range(4):
    a, b = map(int, input().split())
    current_person = current_person + (b-a)
    if max_person < current_person:
        max_person = current_person
print(max_person)
