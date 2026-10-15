"""Duplicate I"""
m = int(input())
n = int(input())

group1 = set()
for _ in range(m):
    line = input()
    group1.add(line)

group2 = set()
for _ in range(n):
    line = input()
    group2.add(line)

common = group1 & group2

if not common:
    print("Nope")
else:
    sorted_ids = sorted(common, reverse=True)
    for _, sid in enumerate(sorted_ids):
        print(sid)
