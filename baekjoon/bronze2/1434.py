# 빈박스 3개 책 3개
# 박스의 용량 5 5 5
# 책의 크기 5 5 5
n, m = map(int, input().split())
box_capacity = list(map(int, input().split()))
book_size = list(map(int, input().split()))
print(sum(box_capacity) - sum(book_size))


