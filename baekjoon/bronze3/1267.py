n = int(input())
arr = list(map(int, input().split()))
youngsik = 0
minsik = 0

for i in range(n):
    youngsik += ((arr[i]//30) * 10)
    minsik += ((arr[i]//60) * 15)
    if arr[i] % 30 < 30:
        youngsik += 10
    if arr[i] % 60 < 60:
        minsik += 15
if minsik < youngsik:
    print('M %d' % minsik)
elif minsik > youngsik:
    print('Y %d'% (youngsik))
else:
    print('Y M %d'% (youngsik))

