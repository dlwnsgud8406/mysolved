state=True
arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] != 0 and arr[i] != 1:
        state=False
if state == True:
    print('S')
elif state == False:
    print('F')
