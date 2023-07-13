import sys
import math
input = sys.stdin.readline
n = int(input())
for i in range(n):
    string = input()
    string = string.replace('\n', '')
    index = math.ceil((len(string))/3)
    mini_string = string[0:index]
    reverse_string = mini_string[::-1]
    tail_string = mini_string[1:index]
    tail_reverse_string = reverse_string[1:index]

    arr = [mini_string + reverse_string + mini_string, mini_string + tail_reverse_string + mini_string, mini_string + reverse_string + tail_string, mini_string + tail_reverse_string + tail_string]
    if string in arr:
        print(1)
    else:
        print(0)
