from collections import deque
def solution(A, B):
    A = deque(list(A))
    B = deque(list(B))
    for i in range(len(A)):
        if A == B:
            return i
        else:
            A.rotate(1)
    return -1
