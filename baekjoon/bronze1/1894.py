for l in open(0):a=[*map(float,l.split())];p=a[2:4]in(a[4:6],a[6:]);s,t=a[2*p:2*p+2];print("%.3f %.3f"%(sum(a[:8:2])-3*s,sum(a[1:8:2])-3*t))
