num = int(input())
const_num = num
answer = 0

while 1:
    a = const_num //10
    b = const_num%10
    c = (a+b) % 10
    const_num = (b*10) + c

    answer += 1
    if(const_num == num):
        break
print(answer)
