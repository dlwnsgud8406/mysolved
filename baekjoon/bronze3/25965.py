import sys

input = sys.stdin.readline
arr_donation = []
game = int(input())
for i in range(game):
    donation = int(input())
    sum = 0
    arr_donation.clear()
    for j in range(donation):
        arr = map(int, input().split())
        arr_donation.extend(arr)
    kill, death, assist = map(int, input().split())
    for k in range(donation):
        current_sum = (kill * arr_donation[3*k]) - (death * arr_donation[3*k + 1]) + (assist * arr_donation[3*k + 2])
        if current_sum > 0 :
            sum += current_sum
    print(sum)

