n, emotion = map(int, input().split())
good_good, good_bad, bad_good, bad_bad = map(float, input().split())
for _ in range(n):
    emotion = emotion * bad_bad + (1-emotion) * good_bad
emotion *= 1000
print(round(1000-emotion), round(emotion))
