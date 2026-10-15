"""Tuple SAD"""
line = input()
parts = line.split(' ')
values = tuple(parts)

target = input()

position = values.index(target)

count = values.count(target)

for _ in range(count):
    for j in range(count):
        if j < count - 1:
            print(position, end=' ')
        else:
            print(position)
