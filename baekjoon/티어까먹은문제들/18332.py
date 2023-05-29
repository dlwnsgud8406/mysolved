

T = input()
T = int(T)
answer = 0
email_list = []
for i in range(0, T):
    email = input()
    check1 = email.split('@')[0]
    check2 = email.split('@')[1]
    if check2.find('.')>-1:
        if check1.find('.')<0:
            answer = answer + 1
print(answer)

