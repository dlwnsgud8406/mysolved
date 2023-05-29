hap, cha = map(int, input().split())
if hap+cha < 0 or hap-cha < 0 or (hap + cha) % 2:
    print(-1)
else:
    big = (hap + cha)//2
    small = hap - big
    print(max(small, big), min(small, big))
