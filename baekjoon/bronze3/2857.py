state = False
for i in range(5):
    name = input()
    if 'FBI' in name:
        print("%d"%(i+1), end=' ')
        state = True
if not state:
    print("HE GOT AWAY!")

