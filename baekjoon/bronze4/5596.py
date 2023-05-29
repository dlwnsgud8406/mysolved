mingook = []
manse = []

mingook = list(map(int, input().split()))
manse = list(map(int, input().split()))

if sum(mingook) >= sum(manse):
    print(sum(mingook))
else:
    print(sum(manse))

