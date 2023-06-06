n = int(input())
if n == 1:
    print(1)
    exit(0)
before_hive = 1
current_hive = 1
count = 0
while 1:
    current_hive = 6 * count + current_hive
    if before_hive < n <= current_hive:
        print(count + 1)
        exit(0)
    before_hive = current_hive
    count += 1

