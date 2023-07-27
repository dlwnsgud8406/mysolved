from collections import Counter
def solution(nums):
    answer = 0
    dict = Counter(nums)
    return min(len(dict), len(nums) // 2)
