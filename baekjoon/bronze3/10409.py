num_work, time = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for i in range(num_work):
    if time < arr[i]:
        break
    else:
        time -= arr[i]
        count += 1
print(count)
