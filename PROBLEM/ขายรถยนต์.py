"""ขายรถยนต์"""
n = int(input())


prices = []
performances = []

for i in range(n):
    p, v = map(int, input().split())
    prices.append(p)
    performances.append(v)


count = 0
max_v = 0


i = n - 1
while i >= 0:
    if performances[i] < max_v:
        count = count + 1

    if performances[i] > max_v:
        max_v = performances[i]

    i = i - 1

print(count)
