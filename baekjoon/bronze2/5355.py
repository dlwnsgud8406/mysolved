dict = {'@' : ' * 3', '%' : ' + 5', '#' : ' - 7'  }
T = int(input())
for i in range(T):
    string = ''
    answer = 0
    for char in input().split():
        if (char == '@') or (char == '%') or (char == '#'):
            answer = eval(string + dict[char])
        else:
            answer = eval(string + char)
        string = str(answer)
    print("%.2f"%(answer))
