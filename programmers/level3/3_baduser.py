import math
from itertools import permutations 
def check(user, ban) : 
    if len(user) != len(ban) : 
        return False 

    else : 
        for i in range(len(user)) :
            if ban[i] == '*' : 
                continue
            else : 
                if user[i] != ban[i] :
                    return False
    return True

def solution(user_id, banned_id) :
    n = len(user_id)
    k = len(banned_id)
    answer = []
    for perm in permutations(user_id, k) : 
        match = True
        for i in range(k) : 
            if check(perm[i], banned_id[i]) is False : 
                match = False
        if match :
            if set(perm) not in answer : 
                answer.append(set(perm))


    return len(answer)