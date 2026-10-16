"""Giraffe"""
n = int(input())
heights = []
for i in range(n):
    h = int(input())
    heights.append(h)

count = 0

for i in range(n):
    satisfied = True
    if i > 0:
        if heights[i] <= heights[i - 1]:
            satisfied = False

    if i < n - 1:
        if heights[i] <= heights[i + 1]:
            satisfied = False

    if satisfied:
        count = count + 1
print(count)
