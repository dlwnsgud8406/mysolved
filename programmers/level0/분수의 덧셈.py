from math import gcd
def solution(numer1, denom1, numer2, denom2):
    count_1 = 1
    a = denom1
    count_2 = 1
    b = denom2
    while denom1 != denom2:
        if denom1 < denom2:
            count_1 += 1
            denom1 += a
        elif denom2 < denom1:
            count_2 += 1
            denom2 += b
    up = numer1*count_1 + numer2*count_2
    down = denom1
    div = gcd(up, down)
    return [up/div, down/div]
