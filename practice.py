a = [1,2,2,3,4,5]
b = [1,1,2,3,4,6]

a_temp = a.copy()
a_result = a.copy()

for i in b:
    if i not in a_temp:
            a_result.append(i)
    else:
        a_temp.remove(i)

# 결과
print(a_result)