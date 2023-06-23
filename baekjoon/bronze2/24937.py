string = 'SciComLove'
n = int(input())
n = n % 10
temp1 = string[0:n]
temp2 = string[n:len(string)]
print(temp2 + temp1)
