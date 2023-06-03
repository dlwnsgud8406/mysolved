info = []
year = []
first_team_name = ''
second_team_name = ''
for i in range(3):
    arr = list(input().split())
    year.append(arr[1])
    info.append(arr)

info.sort(key=lambda x: (-int(x[0]), x[1], x[2]))

year = list(set(sorted(year)))
year = sorted(year)

for i in range(len(year)):
    first_team_name += year[i][2:]

for i in range(len(info)):
    second_team_name += info[i][2][0]
print(first_team_name)
print(second_team_name)

