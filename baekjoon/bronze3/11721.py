import math
string = input()
for i in range(math.ceil(len(string)/10)):
    print(string[i*10 : (i+1)*10])
