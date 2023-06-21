n = int(input())
dict = {}
for i in range(n):
    name, votes = input().split()
    votes = int(votes)
    dict[name] = votes
dict = sorted(dict.items(), key=lambda x: (-x[1], (x[0])))
print(dict[0][0])
