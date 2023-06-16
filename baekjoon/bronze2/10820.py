import sys
input = sys.stdin.readline
while 1:
    string = input()
    if len(string) == 0:
        exit(0)
    else:
        down = 0
        up = 0
        num = 0
        blank = 0
        for char in string:
            if 'A'<=char<='Z':
                up += 1
            elif 'a' <= char <= 'z':
                down += 1
            elif '0' <= char <= '9':
                num += 1
            elif char == ' ':
                blank += 1
        print("%d %d %d %d"%(down, up, num, blank))
