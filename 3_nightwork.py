import heapq

def solution(n, works):
    answer = 0
    if(n<sum(works)):
        works = [-w for w in works]
        heapq.heapify(works)
        for i in range(0, n):
            i = heapq.heappop(works)
            i += 1
            heapq.heappush(works, i)
        answer = sum([w ** 2 for w in works])
    return answer

print(solution(1, [2, 1, 2]))
