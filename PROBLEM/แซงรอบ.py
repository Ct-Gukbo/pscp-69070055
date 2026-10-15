"""แซงรอบ"""
n, k = map(int, input().split())
times = []
for _ in range(n):
    times.append(int(input()))

fastest = min(times)

survivors = 0
for s in times:
    if (k - 1) * s < k * fastest:
        survivors += 1

print(survivors)
