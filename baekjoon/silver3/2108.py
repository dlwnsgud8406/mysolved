import statistics
n = int(input())
arr = [int(input()) for i in range(n)]
a = sorted(statistics.multimode(arr))
print(round(statistics.mean(arr)))
print(statistics.median(arr))
print(a[0] if len(a) == 1 else a[1])
print(max(arr) - min(arr))
