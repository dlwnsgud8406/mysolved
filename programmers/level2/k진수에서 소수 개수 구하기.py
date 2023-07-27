import math
def primenumber(x):
    if x == 1: return False
    for i in range (2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
        	return False
    return True
def solution(n, k):
    answer = 0
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    rev_base = rev_base[::-1]
    string = ''
    for char in rev_base:
        if char == '0':
            if len(string):
                if primenumber(int(string)):
                    answer += 1
            else:
                pass
            string = ''
        else:
            string += char
    if len(string):
        if primenumber(int(string)):
            answer += 1
    return answer
