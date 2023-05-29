per, person = map(int, input().split())
newspaper = list(map(int, input().split()))

real_person = per*person

for i in range(len(newspaper)):
    print('%d'%(newspaper[i] - real_person), end=' ')

