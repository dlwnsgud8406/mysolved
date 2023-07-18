from collections import deque
T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    deq = deque(input().split())
    count = 0
    while 1:
        if any(deq[0] < deq[i] for i in range(1, len(deq))):
            deq.rotate(-1)
        else:
            deq.popleft()
            count += 1
            if m == 0:
                break
        m = (m-1) % len(deq)
    print(count)
