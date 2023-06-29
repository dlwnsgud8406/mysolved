for _ in[0]*int(input()):
    t=''
    while(s:=input())!='':t+=s
    x=round((1-t.count('#')/len(t))*100,1)
    if x==int(x):x=int(x)
    print(f'Efficiency ratio is {x}%.')

# input
# 3
# Pr#nt ex##tly one##ine for#eac# te#t c#se.
#
# None.
#
# The i#put consists of
# N test ca#es. The number
# of th#m (N) is given on
# the first #ine
# of the#input#file.
