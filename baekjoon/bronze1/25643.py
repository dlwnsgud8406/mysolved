r, c = map(int, input().split())
before_row = input()
answer = 1
for _ in range(r-1):
    current_row = input()
    if all(before_row[i:] != current_row[:c-i] for i in range(c)) and all(current_row[i:] != before_row[:c-i] for i in range(c)):
        answer = 0
        break
    before_row = current_row
print(answer)
