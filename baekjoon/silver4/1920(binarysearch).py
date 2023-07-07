import sys

def binary_search(num, arr, left, right):
    while(right >= left):
        middle = (left + right) // 2
        if num == arr[middle]:
            return True
        elif num > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return False

sys.stdin.readline()
answer = sorted(set(sys.stdin.readline().split()))
sys.stdin.readline()
nums = sys.stdin.readline().split()
N = len(answer) - 1

for num in nums:
    print(1 if binary_search(num, answer, 0, N) else 0)
