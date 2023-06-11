import math
def getMyDivisor(n):
    divisorList = []
    for fun_i in range(1, int(n**(1/2)) + 1):
        if(n%fun_i) == 0:
            divisorList.append(fun_i)
            if( (fun_i**2) != n):
                divisorList.append(n//fun_i)
    return len(divisorList)
answer = 1
n = int(input())
for i in range(2, n+1):
    answer += math.ceil(getMyDivisor(i) / 2)

print(answer)
