string = input()
korea = []
yonsei = []
for char in string:
    if char in 'KOREA':
        korea.append(char)
    if char in 'YONSEI':
        yonsei.append(char)
    if korea.count('K') and korea.count('O') and korea.count('R') and korea.count('E') and korea.count('A'):
        print('KOREA')
        exit(0)
    elif yonsei.count('Y') and yonsei.count('O') and yonsei.count('N') and yonsei.count('S') and yonsei.count('E') and yonsei.count('I'):
        print('YONSEI')
        exit(0)
