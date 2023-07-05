def generate_postscript(input_str):
    lines = input_str.strip().split('\n')
    for line in lines:
        length = len(line)
        print("300 420 moveto")
        print("310 420 lineto")
        x, y = 310, 420
        for i in range(length):
            if line[i] == "V":
                y += 10
            elif line[i] == "A":
                y -= 10
            print(f"{x} {y} lineto")
            x += 10
        print("stroke")
        print("showpage")


while 1:
    try:
        str = input()
    except EOFError:
        exit(0)
    else:
        generate_postscript(str)
