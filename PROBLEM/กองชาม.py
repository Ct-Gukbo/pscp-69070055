"""กองชาม"""
n = int(input())

size_counts = [0] * 301

for i in range(n):
    size = int(input())
    size_counts[size] = size_counts[size] + 1

max_stacks = 0
for i in range(1, 301):
    if size_counts[i] > max_stacks:
        max_stacks = size_counts[i]

print(max_stacks)
