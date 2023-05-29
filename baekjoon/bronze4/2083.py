while 1:
    string = input()
    if string == "# 0 0":
        break
    else:
        name, age, weight = string.split()
        if int(age) > 17 or int(weight) >= 80:
            print("%s Senior" % name)
        else:
            print("%s Junior" % name)

