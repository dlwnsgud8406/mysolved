import sys
input = sys.stdin.readline
case = 0
while 1:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        exit(0)
    else:
        answer = 0
        while 1:
            if v >= p:
                v -= p
                answer += l
            else:
                answer += min(v, l)
                case += 1
                break
        print('Case ', case, ': ''%d'%(answer),sep='')
