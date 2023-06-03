input()
string = input()
security_count = 0
bigdata_count = 0
while len(string) > 1:
    if string[0] == 's':
        string = string[8:]
        security_count += 1
    elif string[0] == 'b':
        string = string[7:]
        bigdata_count += 1
if security_count > bigdata_count:
    print('security!')
elif security_count < bigdata_count:
    print('bigdata?')
else:
    print('bigdata? security!')
