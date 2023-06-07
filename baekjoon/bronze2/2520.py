T = int(input())
for i in range(T):
    input()
    milk, egg, sugar, salt, flour = map(int, input().split())
    banana, strawberry, chocolate, wallnut = map(int, input().split())
    min_source = int(min(milk / 8, egg / 8, sugar / 4, salt, flour / 9) * 16)
    with_toping = banana // 1 + strawberry // 30 + chocolate // 25 + wallnut // 10
    print(min(min_source, with_toping))

