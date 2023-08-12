import heapq
def solution(ability, number):
    heapq.heapify(ability)
    for i in range(number):
        smallest1 = heapq.heappop(ability)
        smallest2 = heapq.heappop(ability)
        standard = smallest1 + smallest2
        heapq.heappush(ability, standard)
        heapq.heappush(ability, standard)
    return sum(ability)

print(solution([10, 3, 7, 2], 2))


