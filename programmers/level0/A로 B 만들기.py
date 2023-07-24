def solution(before, after):
    for char in before:
        if before.count(char) != after.count(char):
            return 0
    return 1
