import math
n = list(input())
plastic = []
plastic.append(n.count('0'))
plastic.append(n.count('1'))
plastic.append(n.count('2'))
plastic.append(n.count('3'))
plastic.append(n.count('4'))
plastic.append(n.count('5'))
plastic.append(n.count('7'))
plastic.append(n.count('8'))
plastic.append(math.ceil((n.count('6') + n.count('9')) / 2))
print(max(plastic))
